# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:04:35 2019

@author: fengh
"""

import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import argparse

# Global var to store the ReactToTouch module instance
ReactToTouch = None
memory = None

class ReactToTouch(ALModule):
    '''
    this module able to react to touch events.
    '''
    
    def __init__(self, name):
        ALModule.__init__(self, name)
        '''
        no need IP and port because we have 
        python broker connected to NAOqi broker
        '''
        # create a proxy to altexttospeech for later use
        self.tts = ALProxy("ALTextToSpeech")
        
        # subscribe to touchchanged event:
        global memory
        memory = ALProxy("ALMeory")
        memory.subscribeToEvent("TouchChanged",
                                "ReactToTouch",
                                "onTouched")
        
    def onTouched(self, strVarName, value):
        '''
        this will be called each time a touch 
        is detected.
        '''
        # unscribe to the event when talking, to avoid repetitions
        memory.unsubscribeToEvent("TouchChanged",
                                  "ReactToTouch")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        