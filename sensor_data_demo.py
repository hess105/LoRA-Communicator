"""
Raspperry Pi Pico exercise display on ili9341 SPI Display
using rdagger/micropython-ili9341,
MicroPython ILI9341 Display and XPT2046 Touch Screen Drivers
https://github.com/rdagger/micropython-ili9341
"""
from machine import Pin, SPI
from sys import implementation
from os import uname
import utime

# Screen / Graphics Library
import ili9341

# Text library
from xglcd_font import XglcdFont

# Imports SPI instructions
import mySetup

# Initializes display
display = mySetup.createMyDisplay()

# Defines an unused font
unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)

# Placeholder for user ID
user_id = "Hess:"

# Creates the message storage array
message_array = [["", ""] for _ in range(20)]

# Primary loop
while True:
    
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
    
    # Clears display to avoid overwriting if a new message is smaller than old message
    display.clear()
    
    # Redraws all text stored in the message array
    for i in range(19, -1, -1): 
        display.draw_text8x8(i*10 + 20, 5, message_array[i][0] + " " + message_array[i][1],65535,rotate=90)



