#pip install pyautogui
#using sample.txt
import pyautogui
from time import sleep
import pyperclip


sleep(3)
position = pyautogui.position()
print(position)
pyautogui.doubleClick(x=168, y=570)
sleep(1)
pyautogui.click(x=588, y=120)
pyautogui.hotkey('ctrl', 'a')
sleep(1)
pyautogui.hotkey('ctrl', 'c')
sleep(1)
text = pyperclip.paste()
pyautogui.alert = text
print(text)