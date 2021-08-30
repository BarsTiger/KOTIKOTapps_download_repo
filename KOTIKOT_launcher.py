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

def launchSuperTimer():
    SuperTimerDir = offprojects + "/SuperTimer/"
    SuperTimerUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/SuperTimer/SuperTimer.py"

    if not os.path.exists(SuperTimerDir):
        os.mkdir(SuperTimerDir)

    SuperTimer = SuperTimerDir + "SuperTimer.py"
    urllib.request.urlretrieve(SuperTimerUrl, SuperTimer)

    os.system("python " + SuperTimer)

def launchKotoGameScam():
    KotoGameScamDir = offprojects + "/KotoGameScam/"
    KotoGameScamUrl = "https://github.com/BarsTiger/KOTIKOTapps_download_repo/raw/master/OfficialProjects/KotoGameScam/KotoGameScam.py"

    if not os.path.exists(KotoGameScamDir):
        os.mkdir(KotoGameScamDir)

    KotoGameScam = KotoGameScamDir + "KotoGameScam.py"
    urllib.request.urlretrieve(KotoGameScamUrl, KotoGameScam)

    os.system("python " + KotoGameScam)

def launchNoHiddenText():
    noHiddenTextDir = offprojects + "/noHiddenText/"
    noHiddenTextUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/noHiddenText/noHiddenText.py"

    if not os.path.exists(noHiddenTextDir):
        os.mkdir(noHiddenTextDir)

    noHiddenText = noHiddenTextDir + "noHiddenText.py"
    urllib.request.urlretrieve(noHiddenTextUrl, noHiddenText)

    os.system("python " + noHiddenText)

def launchAutoBridger2():
    autoBridger2Dir = offprojects + "/AutoBridger2/"
    autoBridger2Url = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/AutoBridger2/AutoBridger2.py"

    if not os.path.exists(autoBridger2Dir):
        os.mkdir(autoBridger2Dir)

    autoBridger2 = autoBridger2Dir + "AutoBridger2.py"
    urllib.request.urlretrieve(autoBridger2Url, autoBridger2)

    os.system("python " + autoBridger2)

def launchKotoGTAsingler():
    KotoGTAsinglerDir = offprojects + "/KotoGTAsingler/"
    KotoGTAsinglerUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/KotoGTAsingler/KotoGTAsingler.py"

    if not os.path.exists(KotoGTAsinglerDir):
        os.mkdir(KotoGTAsinglerDir)

    KotoGTAsingler = KotoGTAsinglerDir + "KotoGTAsingler.py"
    urllib.request.urlretrieve(KotoGTAsinglerUrl, KotoGTAsingler)

    os.system("python " + KotoGTAsingler)

def launchKOTO_LAN_Control():
    KOTO_LAN_ControlDir = offprojects + "/KOTO_LAN_Control/"
    KOTO_LAN_ControlUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/KOTO_LAN_Control/KOTO_LAN_Control.py"

    if not os.path.exists(KOTO_LAN_ControlDir):
        os.mkdir(KOTO_LAN_ControlDir)

    KOTO_LAN_Control = KOTO_LAN_ControlDir + "KOTO_LAN_Control.py"
    urllib.request.urlretrieve(KOTO_LAN_ControlUrl, KOTO_LAN_Control)

    os.system("python " + KOTO_LAN_Control)

def launchKotoPythonCompiler():
    KotoPythonCompilerDir = offprojects + "/KotoPythonCompiler/"
    KotoPythonCompilerUrl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/KotoPythonCompiler/KotoPythonCompiler.py"

    if not os.path.exists(KotoPythonCompilerDir):
        os.mkdir(KotoPythonCompilerDir)

    KotoPythonCompiler = KotoPythonCompilerDir + "KotoPythonCompiler.py"
    urllib.request.urlretrieve(KotoPythonCompilerUrl, KotoPythonCompiler)

    os.system("python " + KotoPythonCompiler)

################### Checking buttons #####################
ui.pushButton_1.clicked.connect(launchAutoShipper)
ui.pushButton_2.clicked.connect(launchAutoBridger)
ui.pushButton_3.clicked.connect(launchCatBench)
ui.pushButton_4.clicked.connect(launchautoPageRestarter)
ui.pushButton_5.clicked.connect(launchFilesConnector)
ui.pushButton_6.clicked.connect(launchMeowarch)
ui.pushButton_7.clicked.connect(launchPyQtConverter)
ui.pushButton_8.clicked.connect(launchfileGenerator)
ui.pushButton_9.clicked.connect(launchSuperTimer)
ui.pushButton_10.clicked.connect(launchKotoGameScam)
ui.pushButton_11.clicked.connect(launchNoHiddenText)
ui.pushButton_12.clicked.connect(launchAutoBridger2)
ui.pushButton_13.clicked.connect(launchKotoGTAsingler)
ui.pushButton_14.clicked.connect(launchKOTO_LAN_Control)
ui.actionOpen_settings.triggered.connect(openSettings)

################### Exiting #####################
sys.exit(app.exec_())