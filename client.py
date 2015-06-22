#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# file: client.py

from macroses import BUSNAME, OBJNAME 
import dbus
import sys

bus = dbus.SessionBus()
provider = bus.get_object(BUSNAME, OBJNAME)

def valid_status(status):
    if len(status) > 140:
        print("-- Error: Status length is more than 140 symbols.")
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

if __name__ == "__main__":
    status = None
    try:
        status = sys.argv[1]
    except:
        usage()
        sys.exit(1)
    updateStatus(status)
    

    
