# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:21:29 2019

@author: fengh
"""
# this part is to record , need to be converted to python
#include <iostream>
#include <alproxies/alaudiorecorderproxy.h>
#include <qi/os.hpp>

#int main(int argc, char **argv)
#{
#  if (argc < 2) {
#    std::cerr << "Usage: alaudiorecorder_startrecording pIp"
#              << std::endl;
#    return 1;
#  }
#  const std::string pIp = argv[1];
  channels = ALProxy("ALAudioRecorderProxy", IP, PORT)
#  AL::ALAudioRecorderProxy proxy(pIp);

#  /// Configures the channels that need to be recorded.
  AL::ALValue channels;
  channels.arrayPush(0); #//Left
  channels.arrayPush(0); #//Right
  channels.arrayPush(1); #//Front
  channels.arrayPush(0); #//Rear

#  /// Starts the recording of NAO's front microphone at 16000Hz
#  /// in the specified wav file
  proxy.startMicrophonesRecording("/home/nao/test.wav", "wav", 16000, channels);

  qi::os::sleep(5);

#  /// Stops the recording and close the file after 10 seconds.
  proxy.stopMicrophonesRecording();

  return 0;
}



import sys
import time
from naoqi import ALProxy

if (len(sys.argv) < 2):
    print "Usage: 'python audioplayer_play.py IP [PORT]'"
    sys.exit(1)

IP = sys.argv[1]
PORT = 9559

if (len(sys.argv) > 2):
    PORT = sys.argv[2]
try:
    aup = ALProxy("ALAudioPlayer", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALAudioPlayer"
    print "Error was: ",e
    sys.exit(1)

#plays a file and get the current position 5 seconds later
fileId = aup.post.playFile("/usr/share/naoqi/wav/random.wav")

time.sleep(5)

#currentPos should be near 5 secs
currentPos = aup.getCurrentPosition(fileId)

