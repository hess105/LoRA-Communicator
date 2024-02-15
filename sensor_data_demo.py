from machine import Pin, SPI
from sys import implementation
from os import uname
import utime

# Screen / Graphics Library
from libs import ili9341

# Text library
from libs.xglcd_font import XglcdFont

# Imports SPI instructions
import mySetup

# Import keypad function
import keypad

# Initializes display
display = mySetup.createMyDisplay()

# Defines an unused font
unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)

# Initialize button pin
button = machine.Pin(22, machine.Pin.IN)

# Placeholder for user ID
user_id = "Hess:"

# Creates the message storage array
message_array = [["                    ", "                    "] for _ in range(20)]

### INITIAL DRAWING SECTION. SHOULD NOT NEED TO BE CLEARED

    # Drawing Guidelines
    # x range, 0-240 - Provide a border of 5 px
    # y range, 0-320 - Provide a border of 5 px
    # x init, bottom left with pins on the left side and orientated hotizontal
    # y init, bottom left in same conditions

# Draws display bar at the top
display.fill_hrect(225,5,10,315,65535)
    
# Draws border around currently being typed message
display.draw_rectangle(5,5,15,315,65535)

# Primary loop
while True:
    
    # If statement that if the button value is pressed this loop will execute
    if button.value() == 1:
    
        # Reset text variable
        text = ""
        
        # Check to ensure text length is not too long
        while len(text) == 0 or len(text) > 20:
            text = input("Enter Text:")
        
        # System to shift message data to next column before appending the new message data
        for i in range(19, 0, -1):
            message_array[i][0] = message_array[i - 1][0]
            message_array[i][1] = message_array[i - 1][1]
            
        # Append data to lowest most line
        message_array[0][0] = user_id
        message_array[0][1] = text
        
        
        # Clears last line of text to avoid overwriting if a new message is smaller than old message
        display.fill_hrect(25,5,190,315,0)
        
        
        # Redraws all text stored in the message array
        for i in range(19, -1, -1):
            display.draw_text8x8(i*10 + 25, 5, message_array[i][0] + " " + message_array[i][1],65535,rotate=90)
    
    else:
        print("GPIO 22 is not pulled high")

    # Sleep for 1s
    utime.sleep(1)


