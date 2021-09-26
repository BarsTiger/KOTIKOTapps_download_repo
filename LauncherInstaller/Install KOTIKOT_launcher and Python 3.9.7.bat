@echo off
@echo ----- Downloadig Install-KOTIKOT_launcher from my GitHub ------------------------------------
powershell -command iwr https://raw.githubusercontent.com/BarsTiger/KOTIKOTapps_download_repo/master/LauncherInstaller/Install-KOTIKOT_launcher.py -OutFile Install-KOTIKOT_launcher.py
@echo ----- If you have Python, just close this window now ----------------------------------------
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
@echo ----- Downloadig Python from official site --------------------------------------------------
@echo ----- python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe ------------------------------------
powershell -command iwr https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe -OutFile python.exe
@echo ----- After installing python, run Install-KOTIKOT_launcher to install KOTIKOT_launcher -----
@echo off
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
@echo ----- Running installer... ------------------------------------------------------------------
@start python.exe