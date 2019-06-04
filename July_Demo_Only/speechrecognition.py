# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:32:07 2019

@author: CV_LAB_Howard
"""

#import qi
#import argparse
#import sys
#import time
#from naoqi import ALProxy
#from naoqi import ALBroker
#from naoqi import ALModule
#
#from optparse import OptionParser
#
##NAO_IP = "nao.local"
#
#
## Global variable to store the HumanGreeter module instance
#WordDetected = None
#memory = None
#
#class WordDetectModule(ALModule):
#    """ A simple module able to react
#    to facedetection events
#
#    """
#    def __init__(self, name):
#        ALModule.__init__(self, name)
#        # No need for IP and port here because
#        # we have our Python broker connected to NAOqi broker
#
#        # Create a proxy to ALTextToSpeech for later use
#        self.tts = ALProxy("ALTextToSpeech")
#
#        # Subscribe to the FaceDetected event:
#        global memory
#        memory = ALProxy("ALMemory")
#        memory.subscribeToEvent("WordRecognized",
#            "WordDetected",
#            "onWordDetected")
#
#    def onWordDetected(self, *_args):
#        """ This will be called each time a face is
#        detected.
#
#        """
#        # Unsubscribe to the event when talking,
#        # to avoid repetitions
#        memory.unsubscribeToEvent("WordRecognized",
#            "WordDetected")
#
#        self.tts.say("Hello, you")
#
#        # Subscribe again to the event
#        memory.subscribeToEvent("WordRecognized",
#            "WordDetected",
#            "onWordDetected")
#
#def main(session):
#    """
#    This example uses the ALSpeechRecognition module.
#    """
#    # Get the service ALSpeechRecognition.
#    broker = ALBroker("pythonBroker", "192.168.0.3",9999,"192.168.0.2",9559)
#    asr_service = session.service("ALSpeechRecognition")
#
#    asr_service.setLanguage("English")
#
#    # Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
#    vocabulary = ["yes", "no", "please"]
#    asr_service.setVocabulary(vocabulary, False)
#    asr_service.subscribe("Test_ASR")
#    print 'Speech recognition engine started'
#    time.sleep(10)
#    # Start the speech recognition engine with user Test_ASR
#    asr_service.unsubscribe("Test_ASR")
#    print 'end'
#    try:
#
#        wordModule = WordDetectModule("wordModule")
#        print 'a'
#        prox = ALProxy("ALMemory")
#        print 'b'
#        #prox.insertData("val",1) # forbiden, data is optimized and doesn't manage callback
#        prox.subscribeToEvent("wordModule", "onWordDetected") #  event is case sensitive !
#        print 'c'
#    except Exception,e:
#        print "error"
#        print e
#        exit(1)
#
#    asr_service.subscribe("wordModule")
#    print 'Speech recognition engine started'
#    time.sleep(10)
#    asr_service.unsubscribe("wordModule")
#    print 'end'
#
#
#if __name__ == "__main__":
#    parser = argparse.ArgumentParser()
#    parser.add_argument("--ip", type=str, default="192.168.0.2",
#                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
#    parser.add_argument("--port", type=int, default=9559,
#                        help="Naoqi port number")
#
#    args = parser.parse_args()
#    session = qi.Session()
#    try:
#        session.connect("tcp://" + args.ip + ":" + str(args.port))
#    except RuntimeError:
#        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
#               "Please check your script arguments. Run with -h option for help.")
#        sys.exit(1)
#    main(session)

#from naoqi import ALProxy
#
#import time
#
#data=[]
#ip = "192.168.0.2"
#asr = ALProxy("ALSpeechRecognition", ip, 9559)
#
#asr.pause(True)
#asr.setLanguage("English")
#
#
#vocabulary = ["yes", "no", "please","water usage","Thanks"]
#
#
#asr.setVocabulary(vocabulary, False)
#asr.subscribe(ip)
#memProxy = ALProxy("ALMemory", ip, 9559)
#memProxy.subscribeToEvent('WordRecognized',ip,'wordRecognized')
#
#asr.pause(False)
#
#time.sleep(10)
#
#asr.unsubscribe(ip)
#data=memProxy.getData("WordRecognized")
#print( "data: %s" % data )


from naoqi import *
import time

ROBOT_IP = '192.168.0.2'
#ROBOT_IP = 'marvel.local'

class SpeechRecoModule(ALModule):
    """ A module to use speech recognition """
    def __init__(self, name):
        ALModule.__init__(self, name)
        try:
            self.asr = ALProxy("ALSpeechRecognition")
        except Exception as e:
            self.asr = None
        self.memory = ALProxy("ALMemory")

    def onLoad(self):
        from threading import Lock
        self.bIsRunning = False
        self.mutex = Lock()
        self.hasPushed = False
        self.hasSubscribed = False
        self.BIND_PYTHON(self.getName(), "onWordRecognized")

    def onUnload(self):
        from threading import Lock
        self.mutex.acquire()
        try:
            if (self.bIsRunning):
                if (self.hasSubscribed):
                    self.memory.unsubscribeToEvent("WordRecognized", self.getName())
                if (self.hasPushed and self.asr):
                    self.asr.popContexts()
        except RuntimeError, e:
            self.mutex.release()
            raise e
        self.bIsRunning = False;
        self.mutex.release()

    def onInput_onStart(self):
        from threading import Lock
        self.mutex.acquire()
        if(self.bIsRunning):
            self.mutex.release()
            return
        self.bIsRunning = True
        try:
            if self.asr:
                self.asr.setVisualExpression(True)
                self.asr.pushContexts()
            self.hasPushed = True
            if self.asr:
                self.asr.setVocabulary( ['yes','no'], True )
            self.memory.subscribeToEvent("WordRecognized", self.getName(), "onWordRecognized")
            self.hasSubscribed = True
        except RuntimeError, e:
            self.mutex.release()
            self.onUnload()
            raise e
        self.mutex.release()

    def onWordRecognized(self, key, value, message):
        print 'word recognized'
        if(len(value) > 1 and value[1] >= 0.5):
            print 'recognized the word :', value[0]
        else:
            print 'unsifficient threshold'

global broker; broker = ALBroker("pythonBroker","0.0.0.0", 0, ROBOT_IP, 9559)
global pythonSpeechModule;
pythonSpeechModule = SpeechRecoModule('pythonSpeechModule')
pythonSpeechModule.onLoad()
pythonSpeechModule.onInput_onStart()
time.sleep(10)
pythonSpeechModule.onUnload()