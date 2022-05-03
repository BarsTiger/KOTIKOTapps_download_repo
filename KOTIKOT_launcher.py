import urllib.request
import os
import sys
import subprocess
import requests
import json
try:
    from OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherReminder import popup
except:
    print("[!] Error: KOTIKOTlauncherReminder.py not found, it will be downloaded")

launchfolder = os.getcwd()
offprojects = launchfolder + "/OfficialProjects/"
launcherfiles = offprojects + "/LAUNCHERFILES/"
launcherurl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/KOTIKOT_launcher.py"
guiurl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherMain.py"
reminderurl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherReminder.py"
settingsurl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/KOTIKOTlauncherSettings.py"
launcherversionurl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/v"
appslisturl = "https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/OfficialProjects/LAUNCHERFILES/apps.json"


# ---------------- Checking folders ----------------
if not os.path.exists(offprojects):
    os.mkdir(offprojects)

if not os.path.exists(launcherfiles):
    os.mkdir(launcherfiles)

# ---------------- Self-updataing launcher ----------------
if __name__ == "__main__":
    urllib.request.urlretrieve(appslisturl, launcherfiles + "apps.json")

    try:
        with open(launcherfiles + "/v") as v_file:
            v = int(v_file.read())
    except:
        v = -1

    if v < int(requests.get(launcherversionurl).text):
        urllib.request.urlretrieve(launcherurl, "KOTIKOT_launcher.py")
        urllib.request.urlretrieve(guiurl, launcherfiles + "KOTIKOTlauncherMain.py")
        urllib.request.urlretrieve(reminderurl, launcherfiles + "KOTIKOTlauncherReminder.py")
        urllib.request.urlretrieve(settingsurl, launcherfiles + "KOTIKOTlauncherSettings.py")
        urllib.request.urlretrieve(launcherversionurl, launcherfiles + "v")

        try:
            popup("Launcher updated, please restart it")
        except:
            from OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherReminder import popup
            popup("Launcher updated, please restart it")

        sys.exit(0)


# ---------------- Launching GUI ----------------
import OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherMain as kkui
import OfficialProjects.LAUNCHERFILES.KOTIKOTlauncherSettings as kkset

app = kkui.QtWidgets.QApplication(sys.argv)
KOTIKOTlauncher = kkui.QtWidgets.QMainWindow()
ui = kkui.Ui_KOTIKOTlauncher()
ui.setupUi(KOTIKOTlauncher)
if __name__ == "__main__":
    KOTIKOTlauncher.show()

KOTIKOTsettings = kkset.QtWidgets.QMainWindow()
uiset = kkset.Ui_Form()
uiset.setupUi(KOTIKOTsettings)


# ---------------- Launching programs ----------------
def openSettings():
    KOTIKOTsettings.show()


def downloadApp(app):
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
        downloadApp(app)

    else:
        try:
            with open(directory + "/v") as v_file:
                v = int(v_file.read())
        except:
            v = -1
        if v < int(requests.get('/'.join(app['urls'][0].split('/')[:-1]) + '/v').text):
            print('Current app version is ' + str(v) + ' and new version is '
                  + requests.get('/'.join(app['urls'][0].split('/')[:-1]) + '/v').text)
            print('Updating...')
            downloadApp(app)
            urllib.request.urlretrieve('/'.join(app['urls'][0].split('/')[:-1]) + '/v',
                                       offprojects + app['dir'] + "/v")

    display_name = name.replace('\n', '')
    print(f"---------------- {display_name} ----------------")
    try:
        subprocess.Popen(str(sys.executable + " " if app['runtime'] == "python" else "") + app['run'], cwd=directory,
                         shell=True, close_fds=True)
    except:
        popup('Could not launch ' + display_name + ', please try again', 'Error')
    if not app['window']:
        popup('This app opened in terminal')


# ---------------- Checking buttons ----------------
for button in ui.buttons:
    button.clicked.connect(launchApp)
ui.actionOpen_settings.triggered.connect(openSettings)

# ---------------- Executing and exiting ----------------
if __name__ == "__main__":
    sys.exit(app.exec_())
