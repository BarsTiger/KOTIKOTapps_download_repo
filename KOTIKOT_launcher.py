import urllib.request, os
from subprocess import *
from PyQt5 import *

launchfolder = os.getcwd()
offprojects = launchfolder + "/OfficialProjects/"
launcherfiles = offprojects + "/LAUNCHERFILES/"
launchergithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/KOTIKOT_launcher.py"
launcherguigithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherMain.py"

################### Checking folders #####################
if not os.path.exists(offprojects):
    os.mkdir(offprojects)

if not os.path.exists(launcherfiles):
    os.mkdir(launcherfiles)

################### Self-updataing launcher #####################
urllib.request.urlretrieve(launchergithuburl, "KOTIKOT_launcher.py")
urllib.request.urlretrieve(launcherguigithuburl, launcherfiles + "KOTIKOTlauncherMain.py")

################### Launching GUI #####################
Popen('python ' + launcherfiles + "KOTIKOTlauncherMain.py", shell=True)
