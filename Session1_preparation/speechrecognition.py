# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:32:07 2019

@author: CV_LAB_Howard
"""

from naoqi import *
import time

ROBOT_IP = '192.168.0.3'
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
        self.targetWord = ''
    
    def reset(self):
        self.targetWord = ''

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
                self.asr.setVocabulary( ['yes', 'no', 'help', 'free play', 'copy machine', 'play song', 'exit', 'next', ], True )
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
            self.targetWord = value[0]
            print value[0]
            print len(value[0])
            print ('recognized the word : %s' % value[0])
        else:
            print 'unsifficient threshold'

#global broker; broker = ALBroker("pythonBroker","0.0.0.0", 0, ROBOT_IP, 9559)
#global pythonSpeechModule;
#pythonSpeechModule = SpeechRecoModule('pythonSpeechModule')
#pythonSpeechModule.onLoad()
#pythonSpeechModule.onInput_onStart()
#time.sleep(10)
#pythonSpeechModule.onUnload()