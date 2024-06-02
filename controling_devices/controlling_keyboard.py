#pip install pyautogui
#using sample.txt
import pyautogui
from time import sleep

sleep(3)
position = pyautogui.position()
print(position)
pyautogui.doubleClick(x=172, y=546)
sleep(1)
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write('Python is good too!\n')

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.press( 5 * ['down'])
pyautogui.hotkey('ctrl', 'v')
