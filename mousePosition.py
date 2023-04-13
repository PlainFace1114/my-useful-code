import pyautogui

# wait for the user to left-click the mouse
print("Click anywhere on the screen to get the position...")
while True:
    if pyautogui.mouseDown(button='left'):
        break

# get the position of the mouse pointer
x, y = pyautogui.position()

# print the position
print(f"Clicked position: ({x}, {y})")
