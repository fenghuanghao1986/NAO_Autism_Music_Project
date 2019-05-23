# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:21:29 2019

@author: fengh
"""

import sys
import time
#import argparse
from naoqi import ALProxy


def record(robotIP, PORT, t):
    
    if (len(sys.argv) > 2):
        PORT = sys.argv[2]
    try:
        recordProxy = ALProxy("ALAudioDevice", robotIP, PORT)
    except Exception,e:
        print "Could not create proxy to ALAudioDevice"
        print "Error was: ",e
        sys.exit(1)
        
#    recordProxy = ALProxy("ALAudioDevice", robotIP, PORT)

    recordProxy.startMicrophonesRecording("/home/nao/test.wav");
    print("recording")
    
    time.sleep(t);
    
#      Stops the recording and close the file after 10 seconds.
    recordProxy.stopMicrophonesRecording(); 

def playBack(robotIP, PORT):
    
    if (len(sys.argv) > 2):
        PORT = sys.argv[2]
    try:
        aup = ALProxy("ALAudioPlayer", robotIP, PORT)
    except Exception,e:
        print "Could not create proxy to ALAudioPlayer"
        print "Error was: ",e
        sys.exit(1)
    
#    plays a file and get the current position 5 seconds later
    fileId = aup.post.playFile("/home/nao/test.wav")
    
    time.sleep(5)
    
#    currentPos should be near 5 secs
    currentPos = aup.getCurrentPosition(fileId)
    
#if __name__ == "__main__":
#    parser = argparse.ArgumentParser()
#    parser.add_argument("--ip", type=str, default="192.168.0.6",
#                        help="Robot ip address")
#    parser.add_argument("--port", type=int, default=9559,
#                        help="Robot port number")
#
#    args = parser.parse_args()
#    main(args.ip, args.port)    