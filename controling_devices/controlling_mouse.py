#pip install pyautogui
import pyautogui

position = pyautogui.position()
print(position)
pyautogui.move(100, 0, duration=1)
#pyautogui.moveTo(139, 280, duration=1)
#pyautogui.click(clicks=2)
#pyautogui.doubleClick()
#pyautogui.click(139, 280, button='right')
pyautogui.drag(150, 0, duration = 1, button='left')