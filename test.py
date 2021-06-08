import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

print(time.ctime())


def push():
    os.system('git status ; git commit -a -m "Updated: `date +'%Y-%m-%d %H:%M:%S'`" ; git push origin master')
print("%dffdsfasf")

push()