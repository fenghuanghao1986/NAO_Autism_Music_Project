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
        touched_bodies = []
        for p in value:
            if p[1]:
                touched_bodies.append(p[0])
        
        # subscribe again to the event
        memory.subscribeToEvent("TouchChanged",
                                "ReactToTouch",
                                "onTouched")
        
        
def main(ip, port):
    '''
    we need this broker to be able to construct
    NAOqi modules and subscribe to other modules
    the broker must stay alive until the program
    exists
    '''
    myBroker = ALBroker("myBroker",
                        "0,0,0,0",  # listen to anyone
                        0,          # find a free port and use it
                        ip,         # parent broker IP
                        port)       # parent broker port
    
    global ReactToTouch
    ReactToTouch = ReactToTouch("ReactToTouch")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shtting down"
        myBroker.shutdown()
        sys.exit(0)
        

        
        