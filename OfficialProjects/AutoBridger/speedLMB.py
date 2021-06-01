from pyautogui import *
from keyboard import *
import time
switch = 0
start = 0

while True:
    if is_pressed("r") and start == 0:
        time.sleep(0.02)
        if is_pressed("r") and start == 0:
            start = 1
            switch = 1
    if is_pressed("r") and start == 1:
        time.sleep(0.02)
        if is_pressed("r") and start == 1:
            start = 0
            switch = 0
    if switch == 1:
        click()
