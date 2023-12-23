from pyautogui import *
import pyautogui
import time
import keyboard
import random

Random = ['a', 'w', 's', 'd', '4', 'q', '1', '2', '3', '4']
rand_time = round(random.uniform(0, 5), 2)

conditions = [
    (lambda: pyautogui.locateOnScreen('Team.png', region=(3, 520, 445, 304), grayscale=True, confidence=0.9), "Team.png"),
    (lambda: pyautogui.locateOnScreen('ManuReady.png', region=(0, 538, 447, 528), grayscale=True, confidence=0.7), "ManuReady.png"),
    (lambda: pyautogui.locateOnScreen('InGame.png', region=(87, 755, 379, 304), grayscale=True, confidence=0.5), "InGame.png"),
    (lambda: pyautogui.locateOnScreen('dead.png', grayscale=True, confidence=0.6), "dead.png"),
    (lambda: pyautogui.locateOnScreen('leave.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.6), "leave.png"),
    (lambda: pyautogui.locateOnScreen('space.png', grayscale=True, confidence=0.4), "space.png"),
    (lambda: pyautogui.locateOnScreen('yes.png', region=(506, 550, 912, 304), grayscale=True, confidence=0.6), "yes.png"),
    (lambda: pyautogui.locateOnScreen('jump.PNG', region=(715, 743, 513, 304), grayscale=True, confidence=0.9), "jump.PNG"),
    (lambda: pyautogui.locateOnScreen('Contunue.PNG', region=(773, 581, 379, 304), grayscale=True, confidence=0.6), "Contunue.PNG"),
    (lambda: pyautogui.locateOnScreen('startmanu.PNG', region=(773, 581, 379, 304), grayscale=True, confidence=0.6), "startmanu.PNG"),
]
  
while True:
    for condition, message in conditions:
        try:
            if condition() is not None:
                print(f"Checking for: {message} - Found!", flush=True)
                if message == "Team.png": 
                    pyautogui.click(171, 675)
                    time.sleep(.5)
                    pyautogui.click(171, 675)
                elif message == "ManuReady.png":
                    print("Waiting for game")
                    time.sleep(5)
                elif message == "InGame.png":
                    print("In game waiting")
                    keyboard.press_and_release(Random)
                    time.sleep(rand_time)
                elif message == "dead.png":
                    keyboard.press_and_release('escape')
                    time.sleep(0.5)
                    pyautogui.click(1771, 1040)
                    time.sleep(0.5)
                    pyautogui.click(1771, 1040)
                elif message == "leave.png":
                    pyautogui.click(963, 623)
                    time.sleep(0.5)
                elif message == "space.png":
                    keyboard.press_and_release('space')     
                elif message == "yes.png":
                    pyautogui.click(850, 713)
                    time.sleep(0.5)
                    pyautogui.click(850, 713)
                elif message == "jump.PNG":
                    keyboard.press_and_release('Enter')
                    time.sleep(0.5)
                    keyboard.press_and_release('L')
                    time.sleep(0.5)
                    keyboard.press_and_release('O')
                    time.sleep(0.5)  
                    keyboard.press_and_release('L')
                    time.sleep(0.5)                  
                    keyboard.press_and_release('Enter')
                elif message == "Contunue.PNG":
                    pyautogui.click(952, 717)
                    time.sleep(0.5)
                    pyautogui.click(952, 717)
                elif message == "startmanu.PNG":
                    pyautogui.click(952, 717)
                    time.sleep(0.5)
                    pyautogui.click(952, 717)

        except pyautogui.ImageNotFoundException:
            print(f"Checking for: {message} - Not Found!", flush=True)   
            pass

