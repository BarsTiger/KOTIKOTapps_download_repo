import urllib.request, os

launchfolder = os.getcwd()
kkapps = launchfolder + "\KOTIKOT apps"

if not os.path.exists(kkapps):
    os.mkdir(kkapps)

launcherurl = 'https://raw.githubusercontent.com/BarsTiger/KOTIKOT_launcher/master/KOTIKOT_launcher.py'
urllib.request.urlretrieve(launcherurl, kkapps + "\KOTIKOT_launcher.py")