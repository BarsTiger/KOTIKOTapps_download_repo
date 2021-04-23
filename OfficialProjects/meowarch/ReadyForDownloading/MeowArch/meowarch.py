import os
import easygui
import zipfile
from os.path import basename
import shutil
slash = '\\'
ziporunzip = easygui.buttonbox("What do you want to do?", "Meowarch", ("Archive file", "Unarchive file", "Cancel"))

if ziporunzip == "Cancel":
    exit()


if ziporunzip == "Archive file":
    thisFile = easygui.fileopenbox(filetypes=["*"], multiple=True)
    nameofzip = easygui.enterbox("Enter name of archive:")
    # filenameWithoutTochka = os.path.splitext(thisFile)[0]
    zipfile = zipfile.ZipFile(nameofzip + '.zip', 'w', zipfile.ZIP_DEFLATED)
    for i in range(len(thisFile)):
        zipfile.write(thisFile[i], basename(thisFile[i]))
    while easygui.buttonbox("Do you want to add more files?", "Meowarch", ("Yes", "No, I added all needed files")) == "Yes":
        thisFile = easygui.fileopenbox(filetypes=["*"], multiple=True)
        for i in range(len(thisFile)):
            zipfile.write(thisFile[i], basename(thisFile[i]))
    zipfile.close()
    os.rename(nameofzip + ".zip", nameofzip + ".meowarch")
    wheretosave = easygui.diropenbox("Where to save archive?")
    shutil.move(nameofzip + ".meowarch", wheretosave + slash + nameofzip + ".meowarch")




if ziporunzip == "Unarchive file":
    zipFile = easygui.fileopenbox(filetypes=["*"])
    wheretoextract = easygui.diropenbox("Where to extract files?")
    filenameWithoutTochka = os.path.splitext(zipFile)[0]
    os.rename(zipFile, filenameWithoutTochka + ".zip")
    with zipfile.ZipFile(filenameWithoutTochka + ".zip", 'r') as zipObj:
        zipObj.extractall(wheretoextract)
    os.rename(filenameWithoutTochka + ".zip", filenameWithoutTochka + ".meowarch")