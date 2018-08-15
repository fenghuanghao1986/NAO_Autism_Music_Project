# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 14:40:45 2018

@author: fengh
"""

# this code is to test the very first time NAO play xylophone motion

# import packages
import almath
import argparse
import motion
import sys
import time
from naoqi import ALProxy

maxSpeed = 1.0

def initRobotPosition(motionProxy, postureProxy):
    ''' Inits NAO's position and stiffnesses'''

    motionProxy.wakeUp()
    postureProxy.goToPosture("Crouch", 1.0)
    
    time.sleep(1.0)
    # Make both arms stiff.
    motionProxy.setStiffnesses("LArm", 1.0)
    motionProxy.setStiffnesses("RArm", 1.0)
    # motionProxy.setAngles("LWristYaw", 0.0, 1.0)
    # Make head in the right position and keep stiff.
    motionProxy.setAngles("Head", [0.44, -0.44], 0.5)
    motionProxy.setAngles("RShoulderPitch", )


    # Disable arm moves while walking on left arm.
    motionProxy.setMoveArmsEnabled(False, True)
    time.sleep(1.0)