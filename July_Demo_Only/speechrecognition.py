# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:32:07 2019

@author: CV_LAB_Howard
"""

import qi
import argparse
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

def main(session):
    """
    This example uses the ALSpeechRecognition module.
    """
    # Get the service ALSpeechRecognition.

    asr_service = session.service("ALSpeechRecognition")

    asr_service.setLanguage("English")

    # Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
    vocabulary = ["yes", "no", "please"]
    asr_service.setVocabulary(vocabulary, False)

    # Start the speech recognition engine with user Test_ASR
    asr_service.subscribe("Test_ASR")
    print 'Speech recognition engine started'
    try:

        wordModule = WordDetectModule("wordModule")
        prox = ALProxy("ALMemory")
        #prox.insertData("val",1) # forbiden, data is optimized and doesn't manage callback
        prox.subscribeToEvent("wordModule", "onWordDetected") #  event is case sensitive !
    
    except Exception,e:
        print "error"
        print e
        exit(1)
        
    while (1):
          time.sleep(2)
          
    time.sleep(20)
    asr_service.unsubscribe("Test_ASR")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)