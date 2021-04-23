import urllib.request, os

launchfolder = os.getcwd()
offprojects = launchfolder + "\OfficialProjects"

if not os.path.exists(offprojects):
    os.mkdir(offprojects)
