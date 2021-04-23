import os, shutil, random, easygui, time
from os.path import basename
from subprocess import *
slash = '\\'

start = easygui.buttonbox("Open .ui file to convert it", "Converter", ("Browse file", "Cancel"))

if start == "Cancel":
    exit()

if start == "Browse file":
    thisFile = easygui.fileopenbox(filetypes=["ui"])

filename = basename(thisFile)[:-3]

fileik = open('convert.txt', "w+")
fileik.write('python -m PyQt5.uic.pyuic -x ' + thisFile + " -o " + os.path.dirname(thisFile) + slash + filename + ".py")
fileik.close()

shutil.move("convert.txt", "convert.bat")

call('start convert.bat', shell=True)

time.sleep(1)
os.remove("convert.bat")