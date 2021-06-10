@echo off
start code -n .\log\INFO.log
start python .\natapp_watchdog.py .\
ping localhost -n 3 >nul & start ""  natapp -authtoken=619efe31d8e75603      
