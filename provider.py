#!/usr/bin/env python2
# -*- coding: utf-8 -*-
 
import gobject
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import tweepy
from macroses import BUSNAME, OBJNAME
import sys
from datetime import datetime
import json

class TwitterPoster(dbus.service.Object):
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        busName = dbus.service.BusName(BUSNAME, bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, OBJNAME)
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)
        self.api = tweepy.API(auth)

    @dbus.service.method(BUSNAME, in_signature = 's')
    def updateStatus(self, status):
        try:
            self.api.update_status(status=status)
            log(status)
        except Exception as e:
            error(str(e))

def usage():
    print "Use it like this:"
    print "{0} CONSUMER_KEY CONSUMER_SECRET ACCESS_TOKEN_KEY ACCESS_TOKEN_SECRET".format(sys.argv[0])

def log(t):
    print datetime.now(), "  --  ", t

def error(t):
    log("Error: " + t)

def valid_args(args):
    return len(sys.argv) >= 5

def get_mainloop():
    DBusGMainLoop(set_as_default = True)
    return gobject.MainLoop()

def call_and_exit(fn, args=[], kws={}, result=0):
    fn(*args, **kws)
    sys.exit(result)

if __name__ == "__main__":
    mainloop = get_mainloop() 
    if not valid_args(sys.argv):
        call_and_exit(usage, result=1)
    twitter_poster = TwitterPoster(*sys.argv[1:])
    try:
        print ">>> TwitterPoster started..."
        mainloop.run()
    except KeyboardInterrupt:
        print "\n>>> TwitterPoster stoped!"
        sys.exit(0)
    except Exception as e:
        print "-- Error:", str(e)
