import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

print(time.ctime())


def push():
    os.system('git status ; git add -A ; git commit -m "1"')


push()