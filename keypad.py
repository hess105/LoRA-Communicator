import machine
import utime

# Define keypad matrix
keypad_rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in [0, 1, 2]]
keypad_cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in [3, 4, 5, 6]]

# Define key mapping
keys = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ' ',
    '1': '',
}

def get_letter(key, count):
    if key in keys:
        letters = keys[key]
        return letters[(count - 1) % len(letters)]
    else:
        return None

def scan_keypad():
    pressed_key = None
    
    for i, row in enumerate(keypad_rows):
        row.value(1)
        
        for j, col in enumerate(keypad_cols):
            if col.value() == 1:
                pressed_key = i * len(keypad_cols) + j + 1
                break
        
        row.value(0)
        if pressed_key:
            break
    
    return pressed_key

# Main loop
current_key = None
key_count = 0

while True:
    key = scan_keypad()
    
    if key:
        if key == current_key:
            key_count += 1
        else:
            key_count = 1
            current_key = key
        
        letter = get_letter(str(key), key_count)
        if letter:
            print("Letter entered:", letter)
    
    utime.sleep(0.1)  # Add a small delay to debounce and prevent multiple detections