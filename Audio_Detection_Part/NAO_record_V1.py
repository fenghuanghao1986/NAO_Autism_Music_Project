# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:50:09 2019

@author: CV_LAB_Howard
"""

#import time
#from naoqi import ALProxy
#
#ROBOT_IP = "169.254.254.250"
#
## Creates a proxy on the speech-recognition module
#aar = ALProxy("ALAudioRecorder", ROBOT_IP, 9559)
#
#channels = [1,1,1,1]
#
#aar.startMicrophonesRecording("/home/nao/testttttt.wav", "wav", 48000, channels)
#
#time.sleep(5)
#
#aar.stopMicrophonesRecording()
#
#
### Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
##vocabulary = ["yes", "no", "please"]
##asr.setVocabulary(vocabulary, False)
##
### Start the speech recognition engine with user Test_ASR
##asr.subscribe("Test_ASR")
##print 'Speech recognition engine started'
##time.sleep(20)
##asr.unsubscribe("Test_ASR")

import sys
import time
from naoqi import ALProxy

if __name__ == "__main__":
    IP = "nao.local"  # Replace here with your NaoQi's IP address.
    PORT = 9559

     # Read IP address from first argument if any.
    if len(sys.argv) > 1:
        IP = sys.argv[1]

    videoRecorderProxy = ALProxy("ALVideoRecorder", IP, PORT)

    # This records a 320*240 MJPG video at 10 fps.
    # Note MJPG can't be recorded with a framerate lower than 3 fps.
    videoRecorderProxy.setResolution(1)
    videoRecorderProxy.setFrameRate(10)
    videoRecorderProxy.setVideoFormat("MJPG")
    videoRecorderProxy.startRecording("/home/nao/recordings/cameras", "myvideo")

    time.sleep(5)

    # Video file is saved on the robot in the
    # /home/nao/recordings/cameras/ folder.
    videoInfo = videoRecorderProxy.stopRecording()

    print "Video was saved on the robot: ", videoInfo[1]
    print "Num frames: ", videoInfo[0]