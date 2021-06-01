import urllib.request, os, subprocess, sys

launchfolder = os.getcwd()
kkapps = launchfolder + "/KOTIKOTapps"

if not os.path.exists(kkapps):
    os.mkdir(kkapps)

launcherurl = 'https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/KOTIKOT_launcher.py'
urllib.request.urlretrieve(launcherurl, kkapps + "/KOTIKOT_launcher.py")

try:
    import PyQt5
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQt5'])