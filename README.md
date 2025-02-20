# Auto Clicker

This is a simple Python-based Auto Clicker that allows users to automatically click at a specified position using keyboard controls.

## Features
- Start/stop clicking with the **Enter** key.
- Reset the clicking position to the current mouse position with the **Backspace** key.
- Adjustable clicking speed (default is 0.01 seconds between clicks).
- Runs in the background and listens for keyboard inputs.

## Requirements
This script requires the following Python libraries:
- `pyautogui`
- `pynput`

If these libraries are not installed, you can install them using:
```sh
pip install pyautogui pynput
```

## How to Run
1. Ensure you have Python installed (version 3.x recommended).
2. Install the required dependencies (if not already installed).
3. Run the script using:
   ```sh
   python Auto-clicker.py
   ```
4. Once the script is running:
   - Press **Enter** to start or stop the auto-clicking.
   - Press **Backspace** to reset the clicking position to the current mouse location.
   - To stop the script, press **Ctrl + C** in the terminal.

## Notes
- The script continuously clicks at the last saved position until stopped.
- The delay between clicks can be modified in the `time.sleep(0.01)` line within the script.

## Author
Created by **Joshua's Labs**.

