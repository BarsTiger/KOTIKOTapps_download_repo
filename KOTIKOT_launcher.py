import urllib.request, os

launchfolder = os.getcwd()
offprojects = launchfolder + "\OfficialProjects"
launcherfiles = launchfolder + "\!LAUNCHERFILES"

################### Checking folders #####################
if not os.path.exists(offprojects):
    os.mkdir(offprojects)

if not os.path.exists(launcherfiles):
    os.mkdir(launcherfiles)


