@echo off
start code -n C:\Users\lu\Downloads\natapp_windows_amd64_2_3_9\log\INFO.log
start python C:\Users\lu\Downloads\natapp_windows_amd64_2_3_9\natapp_watchdog.py C:\Users\lu\Downloads\natapp_windows_amd64_2_3_9\
start  ping localhost -n 6 >nul & natapp -authtoken=619efe31d8e75603  
