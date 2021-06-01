hotkeyToBridge = "="
import subprocess, sys
import time
danger = False
try:
    import keyboard
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'keyboard'])
    import keyboard

try:
    from pyautogui import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyautogui'])
    from pyautogui import *

print("AutoBridge started!")
print("To enter SafeMode press Ctrl + 1")

while True:
    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("1") and not danger:
        time.sleep(0.1)
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("1") and not danger:
            danger = True
            print("Okay, hokey is turned OFF (safe mode)")
    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("1") and danger:
        time.sleep(0.1)
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("1") and danger:
            danger = False
            print("Okay, hokey is turned ON (work mode)")
    while keyboard.is_pressed(hotkeyToBridge) and not danger:
        rightClick()
        time.sleep(0.003)
        keyboard.release("shift")
        time.sleep(0.1)
        keyboard.press("s")
        keyboard.press("d")
        keyboard.press("shift")
        time.sleep(0.17)
        if not keyboard.is_pressed(hotkeyToBridge):
            keyboard.release("shift")
            keyboard.release("s")
            keyboard.release("d")
