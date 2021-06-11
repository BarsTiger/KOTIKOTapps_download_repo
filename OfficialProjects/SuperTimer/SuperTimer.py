import time, subprocess, sys, os, urllib.request
try:
    import datetime
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'datetime'])
    import datetime
try:
    from playsound import playsound
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'playsound'])
    from playsound import playsound

superSecond = float(input("Print how many real seconds will be in superSecond: "))
timeInSuperSeconds = int(input("Timer in superSeconds: "))

os.system('cls' if os.name == 'nt' else 'clear')

width = str(len(str(int(timeInSuperSeconds))))
while timeInSuperSeconds > 0:
    print('Time remaining: {{:{:}}} seconds'.format(width).format(timeInSuperSeconds), end='\r')
    timeInSuperSeconds -= 1
    time.sleep(superSecond)
