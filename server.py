# -*- coding: utf-8 -*-
 
import gobject
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import tweepy

BUSNAME = "org.social.TwitterPoster"
OBJ_NAME = "/TwitterPoster"

class TwitterPoster(dbus.service.Object):
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        busName = dbus.service.BusName(BUSNAME, bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, OBJ_NAME)
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)
        self.api = tweepy.API(auth)

    @dbus.service.method(BUSNAME, in_signature = 's')
    def updateStatus(self, status):
        self.api.update_status(status=status)
        print "Update status with:", status

if __name__ == "__main__":
    import sys

    DBusGMainLoop(set_as_default = True)
    mainloop = gobject.MainLoop()
    twitter_poster = TwitterPoster(*sys.argv[1:])
    try:
        print (">>> TwitterPoster started...")
        mainloop.run()
    except KeyboardInterrupt:
        print (">>> TwitterPoster stoped!")
        sys.exit(0)
