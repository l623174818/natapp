@echo off
start code -n C:\Users\lu\Downloads\natapp_windows_amd64_2_3_9\log\INFO.log
start python C:\Users\lu\Downloads\natapp_windows_amd64_2_3_9\natapp_watchdog.py C:\Users\lu\Downloads\natapp_windows_amd64_2_3_9\
ping localhost -n 6 >nul & start ""  natapp -authtoken=619efe31d8e75603  

powershell git status ; powershell git commit -am "Updated" ; powershell git push origin master