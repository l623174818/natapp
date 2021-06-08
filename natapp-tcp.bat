@echo off
start python natapp_watchdog.py C:\Users\lu\Downloads\natapp_windows_amd64_2_3_9
ping -n 2 127.0.0.1>nul $exit
start /wait natapp -authtoken=619efe31d8e75603      
