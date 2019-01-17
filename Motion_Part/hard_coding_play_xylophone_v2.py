# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:08:33 2019

@author: CV_LAB_Howard
"""

import time
import motion
import argparse
from naoqi import ALProxy

def userInitPosture(motionProxy, postureProxy):
    
    # this function should have NAO crouching position with leg joints rest/locked?
    # and both arms should be straight down without touching legs and other parts
     
    postureProxy.goToPosture("Crouch", 1.0)
    time.sleep(1)
    print postureProxy.getPostureFamily()
    
    chainName        = "RArm"
    frame            = motion.FRAME_TORSO
#    transform        = [1.0, 0.0, 0.0, 0.00,
#                        0.0, 1.0, 0.0, 0.00,
#                        0.0, 0.0, 1.0, 0.25]
    transform       = [0.03477038815617561, 0.9961863160133362, 0.080023854970932, 
                       0.0029639352578669786, -0.381715327501297, 0.0872393399477005, 
                       -0.9201536178588867, -0.183818519115448, -0.923625648021698, 
                       0.0014477664371952415, 0.38329294323921204, -0.10117591917514801, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 1.0
    axisMask         = 63 # this value include position and rotation
#    axisMask   = motion.AXIS_MASK_VEL
#    print(motion.AXIS_MASK_VEL)
    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    chainName        = "LArm"
    frame            = motion.FRAME_TORSO
#    transform        = [1.0, 0.0, 0.0, 0.00,
#                        0.0, 1.0, 0.0, 0.00,
#                        0.0, 0.0, 1.0, 0.25]
    transform       = [0.03795033320784569, -0.9755989909172058, -0.21625538170337677, 
                       0.006952085066586733, 0.378103643655777, -0.1863023042678833, 
                       0.9068236947059631, 0.18319708108901978, -0.9249851703643799, 
                       -0.11618120968341827, 0.36180728673934937, -0.10128530114889145, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 1.0
    axisMask         = 63 # this value include position and rotation
#    axisMask   = motion.AXIS_MASK_VEL
#    print(motion.AXIS_MASK_VEL)
    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    
    
    
    

def userSetTransform(motionProxy):

#    # Wake up robot
#    motionProxy.wakeUp()
#
#    # Send robot to Pose Init
#    postureProxy.goToPosture("StandInit", 0.5)

#    time.sleep(4.0)
    # Example showing how to set Torso Transform, using a fraction of max speed
    chainName        = "RArm"
    frame            = motion.FRAME_TORSO
#    transform        = [1.0, 0.0, 0.0, 0.00,
#                        0.0, 1.0, 0.0, 0.00,
#                        0.0, 0.0, 1.0, 0.25]
    transform       = [0.9516681432723999, 0.2406739443540573, 0.19079796969890594, 
                       0.12346550822257996, -0.2703717052936554, 0.9512004852294922, 
                       0.14871717989444733, -0.2338714301586151, -0.1456947773694992, 
                       -0.19311577081680298, 0.9702986478805542, 0.055085137486457825,
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 1.0
    axisMask         = 63 # this value include position and rotation
#    axisMask   = motion.AXIS_MASK_VEL
#    print(motion.AXIS_MASK_VEL)
    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)

#    time.sleep(4.0)

    # Go to rest position
#    motionProxy.rest()
    
    chainName        = "LArm"
    frame            = motion.FRAME_TORSO
#    transform        = [1.0, 0.0, 0.0, 0.00,
#                        0.0, 1.0, 0.0, 0.00,
#                        0.0, 0.0, 1.0, 0.25]
    transform       = [0.9516681432723999, -0.2406739443540573, 0.19079796969890594, 
                       0.12346550822257996, 0.2703717052936554, 0.9512004852294922, 
                       -0.14871717989444733, 0.2338714301586151, -0.1456947773694992, 
                       0.19311577081680298, 0.9702986478805542, 0.055085137486457825, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 1.0
    axisMask         = 63
#    axisMask   = motion.AXIS_MASK_VEL
#    print(motion.AXIS_MASK_VEL)
    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)

def userHitNote(motionProxy):
    
    hit = -1
    fractionMaxSpeed = 1
          
    motionProxy.changeAngles("RWristYaw", hit, fractionMaxSpeed)
    time.sleep(0.04)
        
    motionProxy.setAngles("RWristYaw", -0.4, 1.0)
        
    time.sleep(0.5)
    # motionProxy.changeAngles("RWristYaw", release, 1)        
        
    motionProxy.changeAngles("LWristYaw", -hit, fractionMaxSpeed)        
    time.sleep(0.04)
        
    motionProxy.setAngles("LWristYaw", 0.4, 1.0)
    # motionProxy.changeAngles("LWristYaw", -release, 1)        
    time.sleep(0.5)


    
def main(robotIP, PORT=9559):
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)    
    
    userSetTransform(motionProxy)
    userHitNote(motionProxy)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
#    parser.add_argument("--ip", type=str, default="127.0.0.1",
#                        help="Robot ip address")
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
    