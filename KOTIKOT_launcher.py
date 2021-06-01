import urllib.request, os, time, sys
from subprocess import *
from PyQt5 import *

launchfolder = os.getcwd()
offprojects = launchfolder + "/OfficialProjects/"
launcherfiles = offprojects + "/LAUNCHERFILES/"
launchergithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/KOTIKOT_launcher.py"
launcherguigithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherMain.py"
launcherremindergithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherReminder.py"


################### Checking folders #####################
if not os.path.exists(offprojects):
    os.mkdir(offprojects)

if not os.path.exists(launcherfiles):
    os.mkdir(launcherfiles)

################### Self-updataing launcher #####################
urllib.request.urlretrieve(launchergithuburl, "KOTIKOT_launcher.py")
urllib.request.urlretrieve(launcherguigithuburl, launcherfiles + "KOTIKOTlauncherMain.py")
urllib.request.urlretrieve(launcherremindergithuburl, launcherfiles + "KOTIKOTlauncherReminder.py")

################### Launching GUI #####################
import OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherMain as kkui

app = kkui.QtWidgets.QApplication(sys.argv)
KOTIKOTlauncher = kkui.QtWidgets.QMainWindow()
ui = kkui.Ui_KOTIKOTlauncher()
ui.setupUi(KOTIKOTlauncher)
KOTIKOTlauncher.show()

Popen('python ' + launcherfiles + "KOTIKOTlauncherReminder.py", shell=True)

################### Launching programs (func) #####################
def launchAutoShipper():
    autoShipperDir = offprojects + "/AutoShipper/"
    autoShipperUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/AutoShipper/autoshipper.py"

    if not os.path.exists(autoShipperDir):
        os.mkdir(autoShipperDir)

    autoShipper = autoShipperDir + "autoshipper.py"
    urllib.request.urlretrieve(autoShipperUrl, autoShipper)

    Popen('python ' + autoShipper, shell=True)
    exit()

def launchAutoBridger():
    autoBridgerDir = offprojects + "/AutoBridger/"
    autoBridgerUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/AutoBridger/AutoBridge.py"

    if not os.path.exists(autoBridgerDir):
        os.mkdir(autoBridgerDir)

    autoBridger = autoBridgerDir + "AutoBridge.py"
    urllib.request.urlretrieve(autoBridgerUrl, autoBridger)

    Popen('python ' + autoBridger, shell=True)
    exit()

def launchCatBench():
    CatBenchDir = offprojects + "/CatBench/"
    CatBenchUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/CatBench/CatBench.py"

    if not os.path.exists(CatBenchDir):
        os.mkdir(CatBenchDir)

    CatBench = CatBenchDir + "CatBench.py"
    urllib.request.urlretrieve(CatBenchUrl, CatBench)

    Popen('python ' + CatBench, shell=True)
    exit()

def launchautoPageRestarter():
    autoPageRestarterDir = offprojects + "/autoPageRestarter/"
    autoPageRestarterUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/CoolAutoPressers/autoPageRestarter.py"

    if not os.path.exists(autoPageRestarterDir):
        os.mkdir(autoPageRestarterDir)

    autoPageRestarter = autoPageRestarterDir + "autoPageRestarter.py"
    urllib.request.urlretrieve(autoPageRestarterUrl, autoPageRestarter)

    Popen('python ' + autoPageRestarter, shell=True)
    exit()

def launchFilesConnector():
    FilesConnectorDir = offprojects + "/FilesConnector/"
    FilesConnectorUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/FilesConnector/FilesConnector.py"

    if not os.path.exists(FilesConnectorDir):
        os.mkdir(FilesConnectorDir)

    FilesConnector = FilesConnectorDir + "FilesConnector.py"
    urllib.request.urlretrieve(FilesConnectorUrl, FilesConnector)

    Popen('python ' + FilesConnector, shell=True)
    exit()

def launchPyQtConverter():
    PyQtConverterDir = offprojects + "/PyQtConverter/"
    PyQtConverterUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/PyQtConverter/PyQtConverter.py"

    if not os.path.exists(PyQtConverterDir):
        os.mkdir(PyQtConverterDir)

    PyQtConverter = PyQtConverterDir + "PyQtConverter.py"
    urllib.request.urlretrieve(PyQtConverterUrl, PyQtConverter)

    Popen('python ' + PyQtConverter, shell=True)
    exit()

################### Checking buttons #####################
ui.pushButton_1.clicked.connect(launchAutoShipper)
ui.pushButton_2.clicked.connect(launchAutoBridger)
ui.pushButton_3.clicked.connect(launchCatBench)
ui.pushButton_3.clicked.connect(launchautoPageRestarter)

################### Exiting #####################
sys.exit(app.exec_())