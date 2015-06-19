#!/usr/bin/env python2
# -*- coding: utf-8 -*-
 
import gobject
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import tweepy
from macroses import BUSNAME, OBJNAME
import sys

class TwitterPoster(dbus.service.Object):
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        busName = dbus.service.BusName(BUSNAME, bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, OBJNAME)
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)
        self.api = tweepy.API(auth)

    @dbus.service.method(BUSNAME, in_signature = 's')
    def updateStatus(self, status):
        self.api.update_status(status=status)
        print "Update status with:", status

def usage():
    print("Use it like this:")
    print("{0} CONSUMER_KEY CONSUMER_SECRET ACCESS_TOKEN_KEY ACCESS_TOKEN_SECRET".format(sys.argv[0]))

if __name__ == "__main__":
    DBusGMainLoop(set_as_default = True)
    mainloop = gobject.MainLoop()
    try:
        twitter_poster = TwitterPoster(*sys.argv[1:])
    except:
        usage()
        sys.exit(1)
    try:
        print (">>> TwitterPoster started...")
        mainloop.run()
    except KeyboardInterrupt:
        print ("\n>>> TwitterPoster stoped!")
        sys.exit(0)
