# hotkeyToBridge = input("Which hotkey will be used for bridging: ")
hotkeyToBridge = "="
import subprocess, sys
import time
danger = False
work = False
try:
    import keyboard
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'keyboard'])
    import keyboard

try:
    from pyautogui import *
    import pyautogui
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyautogui'])
    from pyautogui import *
    import pyautogui

pyautogui.PAUSE = 0.0000001

print()
print("AutoBridge started!")
print("To enter SafeMode press Ctrl + 1")
print("To start bridging press and hold " + hotkeyToBridge)
print("To stop bridging and stop going backward on shift press Ctrl+" + hotkeyToBridge)
print()

def fix():
    keyboard.release("shift")
    keyboard.release("s")
    keyboard.release("d")
    print("Fixed!")

def dangermode():
    global danger
    if not danger:
        time.sleep(0.1)
        danger = True
        print("Ok, hotkey is turned OFF (safe mode)")
    elif danger:
        time.sleep(0.1)
        danger = False
        print("Ok, hotkey is turned ON (work mode)")

def ninjabridge():
    global danger
    if not danger:
        keyboard.press("shift")
        keyboard.press("s")
        keyboard.press("d")
        rightClick()
        time.sleep(0.1)
        keyboard.release("shift")
        time.sleep(0.13)
        keyboard.press("shift")
        rightClick()
        time.sleep(0.1013)

keyboard.add_hotkey('ctrl+1', dangermode)
keyboard.add_hotkey(hotkeyToBridge, ninjabridge)
keyboard.add_hotkey(str('ctrl+' + hotkeyToBridge), fix)

keyboard.wait()
