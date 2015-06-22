#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# file: client.py

from client import updateStatus
import readline
import sys

def inputAndUpdate():
    status = raw_input("updateStatus> ")
    if status :
        updateStatus(status)

def mainloop():
    while True:
        inputAndUpdate()

if __name__ == "__main__":
    try:
        mainloop()   
    except KeyboardInterrupt:
        sys.exit(0)
