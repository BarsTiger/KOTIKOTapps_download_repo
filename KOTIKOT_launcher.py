import urllib.request, os, time
from subprocess import *
from PyQt5 import *
from OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherMain import *

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

# Popen('python ' + launcherfiles + "KOTIKOTlauncherMain.py", shell=True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KOTIKOTlauncher = QtWidgets.QMainWindow()
    ui = Ui_KOTIKOTlauncher()
    ui.setupUi(KOTIKOTlauncher)
    KOTIKOTlauncher.show()
    sys.exit(app.exec_())

