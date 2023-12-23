from pyautogui import *
import pyautogui
import time
import keyboard
import random
import subprocess
from datetime import datetime, timedelta
import ctypes
import sys
import os
import json

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
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

# Initialize variables for the timer and counter
start_time = datetime.now()
check_interval = timedelta(minutes=30)
recognized_count = 0

def load_settings():
    try:
        with open("settings.json", "r") as file:
            settings_data = json.load(file)
            return settings_data
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def load_apex_legends_path():
    settings_data = load_settings()
    apex_legends_path = settings_data.get("apex_legends_path", "")
    return apex_legends_path.strip('"')

def save_apex_legends_path(path):
    try:
        with open("settings.json", "r") as file:
            settings_data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        settings_data = {}

    settings_data["apex_legends_path"] = path

    with open("settings.json", "w") as file:
        json.dump(settings_data, file)

# Function to stop Apex Legends
def stop_apex_legends():
    try:
        # Replace 'your_apex_process_name.exe' with the actual process name of Apex Legends
        os.system("taskkill /f /im  r5apex.exe")
        print("Apex Legends stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping Apex Legends: {e}")

# Function to start Apex Legends
def start_apex_legends():
    apex_legends_path = load_apex_legends_path()
    if apex_legends_path:
        try:
            os.startfile(os.path.join(apex_legends_path, "r5apex.exe"))
            print("Apex Legends started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error starting Apex Legends: {e}")
    else:
        print("Apex Legends path not set. Please set the path in the settings.")

while True:
    for condition, message in conditions:
        try:
            if condition() is not None:
                print(f"Checking for: {message} - Found!", flush=True)
                recognized_count += 1
                
                if "InGame.png" in [msg for _, msg in conditions] or "ManuReady.png" in [msg for _, msg in conditions]:
                    print("Resetting the timer and counter.")
                    start_time = datetime.now()
                    recognized_count = 0
                
                if "Jump.PNG" in [msg for _, msg in conditions]:
                    keyboard.press_and_release('Enter')
                    time.sleep(0.5)
                    keyboard.press_and_release('L')
                    time.sleep(0.5)
                    keyboard.press_and_release('O')
                    time.sleep(0.5)
                    keyboard.press_and_release('L')
                    time.sleep(0.5)
                    keyboard.press_and_release('Enter')

                # Your existing actions based on the conditions

        except pyautogui.ImageNotFoundException:
            print(f"Checking for: {message} - Not Found!", flush=True)

    # Check the timer and counter every minute
    if datetime.now() - start_time > check_interval:
        print(f"Game crash detection. Stopping Apex.")
        stop_apex_legends()
        time.sleep(10)
        print(f"Restarting Apex.")
        start_apex_legends()
        recognized_count = 0
        start_time = datetime.now()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
