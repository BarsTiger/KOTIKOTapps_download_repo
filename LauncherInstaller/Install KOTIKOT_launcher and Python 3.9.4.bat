@echo off
@echo ----- Downloadig Python from official site --------------------------------------------------
@echo ----- python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe ------------------------------------
powershell -command iwr https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe -OutFile python-3.9.4-amd64.exe
@echo ----- After installing python, run Install-KOTIKOT_launcher to install KOTIKOT_launcher -----
@echo off
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
@echo ----- Running installer and downloading Install-KOTIKOT_launcher.py ... ---------------------
@start python-3.9.4-amd64.exe
powershell -command iwr https://raw.githubusercontent.com/BarsTiger/KOTIKOT_launcher/master/LauncherInstaller/Install-KOTIKOT_launcher.py -OutFile Install-KOTIKOT_launcher.py