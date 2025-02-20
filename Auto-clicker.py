import pyautogui
import time
from pynput import keyboard

# Initialize variables
clicking = False  # Keeps track of whether clicking is active
x, y = pyautogui.position()  # Default position

def on_press(key):
    global clicking, x, y
    
    try:
        # Enter key pauses/resumes clicking
        if key == keyboard.Key.enter:
            clicking = not clicking
            if clicking:
                print("Clicking...")
            else:
                print("Stopped clicking...")
        
        # Backspace key resets position
        elif key == keyboard.Key.backspace:
            clicking = False  # Pause clicking
            x, y = pyautogui.position()  # Update click position to current mouse position
            print(f"Position reset to {x}, {y}.")
    
    except AttributeError:
        pass

# Keyboard listener to detect key presses
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Autoclicker started. Press Enter to start/stop clicking, Backspace to reset position.\nCreated by Joshua's Labs.")
print("Buy me a coffee?\nSolana: GBeEUoyZPtFi7YwW6t9ZRqW4WRtBHAPzFFrmQTQR298U")

try
    # Main loop for clicking
    while True:
        if clicking:
            pyautogui.click(x, y)
            time.sleep(0.01)  # Adjust speed of clicking here (0.1 seconds between clicks)
except KeyboardInterrupt:
    print("Autoclicker stopped.")
