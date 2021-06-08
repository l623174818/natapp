import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

print(time.ctime())


def push():
    os.system('powershell git status ; powershell git commit -am "Updated" ; powershell git push origin master')

push()
