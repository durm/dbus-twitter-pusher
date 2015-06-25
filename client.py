#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# file: client.py

from macroses import BUSNAME, OBJNAME 
import dbus
import sys
import readline

bus = dbus.SessionBus()
provider = bus.get_object(BUSNAME, OBJNAME)
tweets = []

def valid_status(status):
    if len(status) > 140:
        print("-- Error: Status length ({0}) is more than 140 symbols.".format(str(len(status))))
        return False
    return True

def updateStatus(status):
    if valid_status(status):
        try:    
            provider.updateStatus(status, dbus_interface = BUSNAME)
        except Exception as e:
            print("-- Error:", str(e))

def usage():
    print("Use it like this:")
    print("{0} {1}".format(sys.argv[0], "\"status\""))

def inputAndUpdate():
    status = raw_input("updateStatus> ")
    if status :
        updateStatus(status)

def mainloop():
    while True:
        inputAndUpdate()

if __name__ == "__main__":
    timeline()
    if len(sys.argv) == 1 :
        try:
            mainloop()   
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        updateStatus(sys.argv[1])

    
