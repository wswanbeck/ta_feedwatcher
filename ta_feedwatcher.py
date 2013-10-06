#!/usr/bin/env python
# encoding: utf-8
from lib.websocket import create_connection
from lib.taconfig import TaConfig
import sys
import time
import urllib2

def watchfeeds(config_path):
    theconfig = TaConfig(config_path)
    """
    ws=create_connection("ws://localhost:9000/")
    if (ws is None):
        print ("Argggggg")
    ws.send("test111")
    ws.close()
    """

    # run forever - reading feeds and posting to websocket
    while 1:
        for feed in theconfig.feeds:
             # read from feedurl
             try:
                 print "reading from " + feed.url
                 response = urllib2.urlopen(str(feed.url))
                 feeddata = response.read()
                 response.close()

                 try:
                     websockaddress = "ws://" + feed.websocket_host + ":" + feed.websocket_port + "/"
                     print "posting to websocket at " + websockaddress
                     c = create_connection(websockaddress)
                     c.send("test1")
                     c.send(str(feeddata))
                     c.send("test2")
                     c.close()
                 except:
                     print "*** error attempting to post to websocket at " + feed.websocket_host + ":" + feed.websocket_port

             except:
                 print "*** error attempting to read " + feed.url
        time.sleep(10)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "No config file given!"
        exit()
    configpath = sys.argv[1]
    watchfeeds(configpath)