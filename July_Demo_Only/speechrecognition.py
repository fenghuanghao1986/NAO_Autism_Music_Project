# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:32:07 2019

@author: CV_LAB_Howard
"""

import time
from naoqi import ALProxy


ROBOT_IP = "your.robot.ip.here"

# Creates a proxy on the speech-recognition module
asr = ALProxy("ALSpeechRecognition", ROBOT_IP, 9559)

asr.setLanguage("English")

# Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
vocabulary = ["yes", "no", "please"]
asr.setVocabulary(vocabulary, False)

# Start the speech recognition engine with user Test_ASR
asr.subscribe("Test_ASR")
print 'Speech recognition engine started'
time.sleep(20)
asr.unsubscribe("Test_ASR")