import urllib.request
import os
import sys
import subprocess
import requests
import json

launchfolder = os.getcwd()
offprojects = launchfolder + "/OfficialProjects/"
launcherfiles = offprojects + "/LAUNCHERFILES/"
launchergithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/KOTIKOT_launcher.py"
launcherguigithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherMain.py"
launcherremindergithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherReminder.py"
launchersettingsgithuburl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherSettings.py"


# ---------------- Checking folders ----------------
if not os.path.exists(offprojects):
    os.mkdir(offprojects)

if not os.path.exists(launcherfiles):
    os.mkdir(launcherfiles)

# ---------------- Self-updataing launcher ----------------
# if __name__ == "__main__":
    # urllib.request.urlretrieve(launchergithuburl, "KOTIKOT_launcher.py")
    # urllib.request.urlretrieve(launcherguigithuburl, launcherfiles + "KOTIKOTlauncherMain.py")
    # urllib.request.urlretrieve(launcherremindergithuburl, launcherfiles + "KOTIKOTlauncherReminder.py")
    # urllib.request.urlretrieve(launchersettingsgithuburl, launcherfiles + "KOTIKOTlauncherSettings.py")


# ---------------- Launching GUI ----------------
import OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherMain as kkui
import OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherSettings as kkset
import OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherReminder as kkrem

app = kkui.QtWidgets.QApplication(sys.argv)
KOTIKOTlauncher = kkui.QtWidgets.QMainWindow()
ui = kkui.Ui_KOTIKOTlauncher()
ui.setupUi(KOTIKOTlauncher)
if __name__ == "__main__":
    KOTIKOTlauncher.show()

KOTIKOTsettings = kkset.QtWidgets.QMainWindow()
uiset = kkset.Ui_Form()
uiset.setupUi(KOTIKOTsettings)

KOTIKOTreminder = kkrem.QtWidgets.QMainWindow()
uirem = kkrem.Ui_Form()
uirem.setupUi(KOTIKOTreminder)


# ---------------- Launching programs ----------------
def openSettings():
    KOTIKOTsettings.show()


def download_app(app):
    for url in app['urls']:
        print('Downloading ' + url)
        urllib.request.urlretrieve(url, offprojects + app['dir'] + "/" + url.split("/")[-1])
    print('Finished')


def launchApp():
    with open("OfficialProjects/LAUNCHERFILES/apps.json") as appsfile:
        apps = json.load(appsfile)
    name = KOTIKOTlauncher.sender().text()
    app = apps[name]
    directory = offprojects + app['dir']

    if not os.path.exists(directory):
        os.mkdir(directory)
        download_app(app)

    else:
        with open(directory + "/v") as v_file:
            v = int(v_file.read())
        if v < int(requests.get('/'.join(app['urls'][0][:-1])).text):
            print('bebras')
            download_app(app)


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


# ---------------- Checking buttons ----------------
for button in ui.buttons:
    button.clicked.connect(launchApp)
ui.actionOpen_settings.triggered.connect(openSettings)

# ---------------- Executing and exiting ----------------
if __name__ == "__main__":
    sys.exit(app.exec_())
