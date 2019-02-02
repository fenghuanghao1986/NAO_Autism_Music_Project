# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:50:09 2019

@author: CV_LAB_Howard
"""

import time
from naoqi import ALProxy

ROBOT_IP = "169.254.254.250"

# Creates a proxy on the speech-recognition module
aar = ALProxy("ALAudioRecorder", ROBOT_IP, 9559)

channels = [1,1,1,1]

aar.startMicrophonesRecording("/home/nao/testttttt.wav", "wav", 48000, channels)

time.sleep(5)

aar.stopMicrophonesRecording()


## Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
#vocabulary = ["yes", "no", "please"]
#asr.setVocabulary(vocabulary, False)
#
## Start the speech recognition engine with user Test_ASR
#asr.subscribe("Test_ASR")
#print 'Speech recognition engine started'
#time.sleep(20)
#asr.unsubscribe("Test_ASR")

