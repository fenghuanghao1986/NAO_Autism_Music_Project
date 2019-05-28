# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:36:09 2019

@author: CV_LAB_Howard
"""

import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "nao.local"


# Global variable to store the HumanGreeter module instance
WordDetected = None
memory = None


class WordDetectModule(ALModule):
    """ A simple module able to react
    to facedetection events

    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")

        # Subscribe to the FaceDetected event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("WordRecognized",
            "WordDetected",
            "onWordDetected")

    def onWordDetected(self, *_args):
        """ This will be called each time a face is
        detected.

        """
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("WordRecognized",
            "WordDetected")

        self.tts.say("Hello, you")

        # Subscribe again to the event
        memory.subscribeToEvent("WordRecognized",
            "WordDetected",
            "onWordDetected")

