import pyautogui
import time

while True: 
    pyautogui.moveRel(10,0,duration=0.2)
    time.sleep(1)
    pyautogui.moveRel(-10,0,duration=0.2)
    time.sleep(1)
