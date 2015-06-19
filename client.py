# -*- coding: utf-8 -*-
# file: client.py

from macroses import BUSNAME, OBJNAME 
import dbus

bus = dbus.SessionBus()
provider = bus.get_object(BUSNAME, OBJNAME)

def updateStatus(status):
    provider.updateStatus(status, dbus_interface = BUSNAME)

if __name__ == "__main__":
    import sys
    updateStatus(sys.argv[1])
    

    