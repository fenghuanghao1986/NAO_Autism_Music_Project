# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:38:37 2019

@author: CV_LAB_Howard
"""

import motion
import argparse
import time
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    motionProxy.rest()
    motionProxy.setStiffnesses("LArm", 0)
    motionProxy.setStiffnesses("RArm", 1)
    
    time.sleep(1)
        
    # Example showing how to get the end of the right arm as a transform
    # represented in torso space. The result is a 4 by 4 matrix composed
    # of a 3*3 rotation matrix and a column vector of positions.
    
    name  = 'RArm'
    print(name)
    frame  = motion.FRAME_TORSO
    useSensorValues  = False
    transResult = motionProxy.getPosition(name, frame, useSensorValues)
    angResult = motionProxy.getAngles(name, useSensorValues)
    print(angResult)
    print(transResult)
    
#    name = 'RWristYaw'
#    print(name)
#    angResult = motionProxy.getAngles(name, useSensorValues)
#    print(angResult)
#    posResult = motionProxy.getPosition(name, frame, useSensorValues)
#    print(posResult)
    
    
    chainName        = 'RArm'
    frame            = motion.FRAME_TORSO

    transform       = [0.13809768855571747, -0.1352280229330063, -0.05866047367453575, 1.5619783401489258, 0.6344230771064758, -0.2303130328655243]
    
    fractionMaxSpeed = 0.5
    axisMask         = 63

    motionProxy.setPosition(chainName, frame, transform, fractionMaxSpeed, axisMask)
    time.sleep(1)
    
    transResult = motionProxy.getPosition(name, frame, useSensorValues)
    angResult = motionProxy.getAngles(name, useSensorValues)
    print(angResult)
    print(transResult)
##    
#    hit = -0.25
#    fractionMaxSpeed = 0.2
#          
#    motionProxy.changeAngles("LWristYaw", hit, fractionMaxSpeed)
#    time.sleep(3)
#    
#    newAng = motionProxy.getAngles("LWristYaw", useSensorValues)
#    time.sleep(3)
#    print(newAng)
##    
#    newTrans = motionProxy.getTransform('LArm', frame, useSensorValues)
#    print(newTrans)

    
#    names      = ["RWristYaw"]
#    angleLists = [[-105*almath.TO_RAD, -55*almath.TO_RAD]]
#    timeLists  = [[0.05, 0.08]]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)