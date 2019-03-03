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
    motionProxy.setStiffnesses("LArm", 0)
    motionProxy.setStiffnesses("RArm", 1)
#    motionProxy.rest()
    # Example showing how to get the end of the right arm as a transform
    # represented in torso space. The result is a 4 by 4 matrix composed
    # of a 3*3 rotation matrix and a column vector of positions.
    name  = 'RArm'
    print(name)
    frame  = motion.FRAME_TORSO
    useSensorValues  = True
    transResult = motionProxy.getTransform(name, frame, useSensorValues)
    print(transResult)
    
    name = "RWristYaw"
    print(name)
    angResult = motionProxy.getAngles(name, useSensorValues)
    print(angResult)
    

#    chainName        = "LArm"
#    frame            = motion.FRAME_TORSO
#
#    transform       = [0.8993398547172546, -0.3961007595062256, 0.1851811408996582, 0.1086173802614212, 0.43249425292015076, 0.7435457110404968, -0.5099887251853943, 0.23731710016727448, 0.0643162727355957, 0.5387429594993591, 0.8400115966796875, 0.03261344134807587, 0.0, 0.0, 0.0, 1.0]
#    
#    fractionMaxSpeed = 0.5
#    axisMask         = 63
#
#    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
#    time.sleep(1)
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