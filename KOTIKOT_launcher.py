import urllib.request, os, time, sys
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
# urllib.request.urlretrieve(launchergithuburl, "KOTIKOT_launcher.py")
urllib.request.urlretrieve(launcherguigithuburl, launcherfiles + "KOTIKOTlauncherMain.py")

################### Launching GUI #####################
# Popen('python ' + launcherfiles + "KOTIKOTlauncherMain.py", shell=True)
import OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherMain as kkui

app = kkui.QtWidgets.QApplication(sys.argv)
KOTIKOTlauncher = kkui.QtWidgets.QMainWindow()
ui = kkui.Ui_KOTIKOTlauncher()
ui.setupUi(KOTIKOTlauncher)
KOTIKOTlauncher.show()

################### Launching programs (func) #####################
def launchAutoShipper():
    print("meow")

################### Checking buttons #####################
ui.pushButton_1.clicked.connect(launchAutoShipper)


################### Exiting #####################
sys.exit(app.exec_())