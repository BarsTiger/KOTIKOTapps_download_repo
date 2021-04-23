import keyboard
import time

print("Auto page restarter by BarsTiger")
print("You have 5 sec for going to browser")
time.sleep(5)

while True:
    keyboard.press("ctrl")
    keyboard.press("r")
    time.sleep(0.5)
    keyboard.release("ctrl")
    keyboard.release("r")
    time.sleep(0.5)
    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("1"):
        exit()
