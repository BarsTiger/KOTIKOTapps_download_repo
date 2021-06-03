import urllib.request, os, time, sys, subprocess
from subprocess import *
from PyQt5 import *

launchfolder = os.getcwd()
offprojects = launchfolder + "/OfficialProjects/"
launcherfiles = offprojects + "/LAUNCHERFILES/"
launchergithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/KOTIKOT_launcher.py"
launcherguigithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherMain.py"
launcherremindergithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherReminder.py"
launchersettingsgithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherSettings.py"

################### Checking folders #####################
if not os.path.exists(offprojects):
    os.mkdir(offprojects)

if not os.path.exists(launcherfiles):
    os.mkdir(launcherfiles)

################### Self-updataing launcher #####################
urllib.request.urlretrieve(launchergithuburl, "KOTIKOT_launcher.py")
urllib.request.urlretrieve(launcherguigithuburl, launcherfiles + "KOTIKOTlauncherMain.py")
urllib.request.urlretrieve(launcherremindergithuburl, launcherfiles + "KOTIKOTlauncherReminder.py")
urllib.request.urlretrieve(launchersettingsgithuburl, launcherfiles + "KOTIKOTlauncherSettings.py")


################### Launching GUI #####################
import OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherMain as kkui
import OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherSettings as kkset

app = kkui.QtWidgets.QApplication(sys.argv)
KOTIKOTlauncher = kkui.QtWidgets.QMainWindow()
ui = kkui.Ui_KOTIKOTlauncher()
ui.setupUi(KOTIKOTlauncher)
KOTIKOTlauncher.show()

settings = kkset.QtWidgets.QApplication(sys.argv)
KOTIKOTsettings = kkset.QtWidgets.QMainWindow()
uiset = kkset.Ui_Form()
uiset.setupUi(KOTIKOTsettings)

Popen('python ' + launcherfiles + "KOTIKOTlauncherReminder.py", shell=True)

################### Launching programs (func) #####################
def openSettings():
    KOTIKOTsettings.show()

def launchAutoShipper():
    autoShipperDir = offprojects + "/AutoShipper/"
    autoShipperUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/AutoShipper/autoshipper.py"

    if not os.path.exists(autoShipperDir):
        os.mkdir(autoShipperDir)

    autoShipper = autoShipperDir + "autoshipper.py"
    urllib.request.urlretrieve(autoShipperUrl, autoShipper)

    os.system("python " + autoShipper)

def launchAutoBridger():
    autoBridgerDir = offprojects + "/AutoBridger/"
    autoBridgerUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/AutoBridger/AutoBridge.py"

    if not os.path.exists(autoBridgerDir):
        os.mkdir(autoBridgerDir)

    autoBridger = autoBridgerDir + "AutoBridge.py"
    urllib.request.urlretrieve(autoBridgerUrl, autoBridger)

    os.system("python " + autoBridger)

def launchCatBench():
    CatBenchDir = offprojects + "/CatBench/"
    CatBenchUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/CatBench/CatBench.py"

    if not os.path.exists(CatBenchDir):
        os.mkdir(CatBenchDir)

    CatBench = CatBenchDir + "CatBench.py"
    urllib.request.urlretrieve(CatBenchUrl, CatBench)

    os.system("python " + CatBench)

def launchautoPageRestarter():
    autoPageRestarterDir = offprojects + "/autoPageRestarter/"
    autoPageRestarterUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/CoolAutoPressers/autoPageRestarter.py"

    if not os.path.exists(autoPageRestarterDir):
        os.mkdir(autoPageRestarterDir)

    autoPageRestarter = autoPageRestarterDir + "autoPageRestarter.py"
    urllib.request.urlretrieve(autoPageRestarterUrl, autoPageRestarter)

    os.system("python " + autoPageRestarter)

def launchFilesConnector():
    FilesConnectorDir = offprojects + "/FilesConnector/"
    FilesConnectorUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/FilesConnector/FilesConnector.py"

    if not os.path.exists(FilesConnectorDir):
        os.mkdir(FilesConnectorDir)

    FilesConnector = FilesConnectorDir + "FilesConnector.py"
    urllib.request.urlretrieve(FilesConnectorUrl, FilesConnector)

    os.system("python " + FilesConnector)

def launchMeowarch():
    meowarchDir = offprojects + "/meowarch/"
    meowarchUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/meowarch/meowarch.py"

    if not os.path.exists(meowarchDir):
        os.mkdir(meowarchDir)

    meowarch = meowarchDir + "meowarch.py"
    urllib.request.urlretrieve(meowarchUrl, meowarch)

    os.system("python " + meowarch)

def launchPyQtConverter():
    PyQtConverterDir = offprojects + "/PyQtConverter/"
    PyQtConverterUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/PyQtConverter/PyQtConverter.py"

    if not os.path.exists(PyQtConverterDir):
        os.mkdir(PyQtConverterDir)

    PyQtConverter = PyQtConverterDir + "PyQtConverter.py"
    urllib.request.urlretrieve(PyQtConverterUrl, PyQtConverter)

    os.system("python " + PyQtConverter)

def launchfileGenerator():
    fileGeneratorDir = offprojects + "/fileGenerator/"
    fileGeneratorUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/RandomBigOrSmallFileCreator/fileGenerator.py"

    if not os.path.exists(fileGeneratorDir):
        os.mkdir(fileGeneratorDir)

    fileGenerator = fileGeneratorDir + "fileGenerator.py"
    urllib.request.urlretrieve(fileGeneratorUrl, fileGenerator)

    os.system("python " + fileGenerator)


################### Checking buttons #####################
ui.pushButton_1.clicked.connect(launchAutoShipper)
ui.pushButton_2.clicked.connect(launchAutoBridger)
ui.pushButton_3.clicked.connect(launchCatBench)
ui.pushButton_4.clicked.connect(launchautoPageRestarter)
ui.pushButton_5.clicked.connect(launchFilesConnector)
ui.pushButton_6.clicked.connect(launchMeowarch)
ui.pushButton_7.clicked.connect(launchPyQtConverter)
ui.pushButton_8.clicked.connect(launchfileGenerator)
ui.actionOpen_settings.triggered.connect(openSettings)

################### Exiting #####################
sys.exit(app.exec_())
sys.exit(settings.exec_())