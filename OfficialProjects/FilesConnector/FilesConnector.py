import os, time, subprocess, sys
from os.path import basename
from subprocess import *
try:
    import easygui
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'easygui'])
    import easygui

slash = '/'

start = easygui.buttonbox("Open file (image, text, sound, what you want) to push archive in", "FilesConnector", ("Browse file", "Cancel"))

if start == "Cancel":
    exit()

if start == "Browse file":
    thisFile = easygui.fileopenbox(filetypes=["*.mp3", "*.jpg", "*.png", "*.txt", "*.banana", "*.allWhatYouWant"])

start = easygui.buttonbox("Open archive", "FilesConnector", ("Browse archive", "Cancel"))

if start == "Cancel":
    exit()

if start == "Browse archive":
    thisArchive = easygui.fileopenbox(filetypes=["*.rar", "*.zip", "*.7z", "*.meowarch", "*.RandomArch", "*.allWhatYouWant"])

filename, file_extension = os.path.splitext(thisFile)
archname, arch_extension = os.path.splitext(thisFile)

nameofreadyfile = easygui.enterbox("Enter name of hidden archive:") + file_extension

start = easygui.buttonbox("Now, choose folder to save hidden archive in", "FilesConnector", ("Browse folder", "Cancel"))
if start == "Cancel":
    exit()

if start == "Browse folder":
    wheretosave = easygui.diropenbox("Where to save archive?")

batnik = open('connect.bat', "w+")
batnik.write('copy /b ' + thisFile + "+" + thisArchive + " " + wheretosave + slash + nameofreadyfile)
batnik.close()

call('start connect.bat', shell=True)
time.sleep(1)
os.remove("connect.bat")
