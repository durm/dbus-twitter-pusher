#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# file: client.py

from macroses import BUSNAME, OBJNAME 
import dbus
import sys

bus = dbus.SessionBus()
provider = bus.get_object(BUSNAME, OBJNAME)

def updateStatus(status):
    provider.updateStatus(status, dbus_interface = BUSNAME)

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
    

    
