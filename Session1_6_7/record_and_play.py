# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:21:29 2019

@author: fengh
"""
# this part is to record , need to be converted to python
#include <iostream>
#include <alproxies/alaudiorecorderproxy.h>
#include <qi/os.hpp>

import sys
import time
import argparse
from naoqi import ALProxy

#int main(int argc, char **argv)
#{
#  if (argc < 2) {
#    std::cerr << "Usage: alaudiorecorder_startrecording pIp"
#              << std::endl;
#    return 1;
#  }
#  const std::string pIp = argv[1];

def main(robotIP, PORT):
    recordProxy = ALProxy("ALAudioDevice", robotIP, PORT)
    #  AL::ALAudioRecorderProxy proxy(pIp);
    
    #  /// Configures the channels that need to be recorded.
#    channelsProxy = ALProxy("ALValue", robotIP, PORT)
#    #  AL::ALValue channels;
#    channelsProxy.arrayPush(0); #//Left
#    channelsProxy.arrayPush(0); #//Right
#    channelsProxy.arrayPush(1); #//Front
#    channelsProxy.arrayPush(0); #//Rear
    
    #  /// Starts the recording of NAO's front microphone at 24000Hz
    #  /// in the specified wav file
    recordProxy.startMicrophonesRecording("/home/nao/test.wav");
    print("recording")
    time.sleep(10);
    
    #  /// Stops the recording and close the file after 10 seconds.
    recordProxy.stopMicrophonesRecording(); 

#    if (len(sys.argv) < 2):
#        print "Usage: 'python audioplayer_play.py IP [PORT]'"
#        sys.exit(1)
#    
#    IP = sys.argv[1]
#    PORT = 9559
    
    if (len(sys.argv) > 2):
        PORT = sys.argv[2]
    try:
        aup = ALProxy("ALAudioPlayer", robotIP, PORT)
    except Exception,e:
        print "Could not create proxy to ALAudioPlayer"
        print "Error was: ",e
        sys.exit(1)
    
    #plays a file and get the current position 5 seconds later
    fileId = aup.post.playFile("/home/nao/test.wav")
    
    time.sleep(5)
    
    #currentPos should be near 5 secs
    currentPos = aup.getCurrentPosition(fileId)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.6",
                        help="Robot ip address")
#    parser.add_argument("--ip", type=str, default="127.0.0.1",
#                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)    