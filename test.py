import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

print(time.ctime())


# def push():
#     os.system('powershell git status ; git add -A ; powershell git commit -m "Updated: $(Get-Date)" ; powershell git push origin master')

# push()

os.system('powershell git status')
os.system('powershell git add -A')
os.system('powershell git commit -m "Updated: $(Get-Date)"')
os.system('powershell git push origin master')