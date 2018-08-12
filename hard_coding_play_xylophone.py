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

lArm = "LArm"
rArm = "RArm"
maxSpeed   = 1.0

def initRobotPosition(motionProxy, postureProxy):
    ''' Inits NAO's position and stiffnesses'''
    
    global lArm
    global rArm
    
    motionProxy.wakeUp()
    postureProxy.goToPosture("Crouch", 1.0)
    
    time.sleep(1.0)
    # Make left arm loose.
    motionProxy.setAngles("LWristYaw", 0.0, 1.0)
    motionProxy.setAngles("Head", [0.44, -0.44], 0.5)
    motionProxy.setStiffnesses(lArm, 1.0)
    motionProxy.setStiffnesses(rArm, 1.0)
    motionProxy.setStiffnesses("LWristYaw", 0.2)

    # Disable arm moves while walking on left arm.
    motionProxy.setMoveArmsEnabled(False, True)
    time.sleep(1.0)