# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 21:43:11 2019

@author: CV_LAB_Howard
"""

import time
import motion
import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Pose Init
#    postureProxy.goToPosture("Crouch", 0.5)

#    time.sleep(4.0)
    # Example showing how to set Torso Transform, using a fraction of max speed
    chainName        = "LArm"
    frame            = motion.FRAME_TORSO
    transform       = [0.9669263362884521, -0.18347570300102234, 0.17717286944389343, 0.14802011847496033, 0.1927211582660675, 0.9805812835693359, -0.03631642460823059, 0.20442283153533936, -0.167069211602211, 0.06926026940345764, 0.9835095405578613, 0.01827755756676197, 0.0, 0.0, 0.0, 1.0]

    fractionMaxSpeed = 0.5
    axisMask         = 63
#    axisMask   = motion.AXIS_MASK_VEL

    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    chainName        = "RArm"
    frame            = motion.FRAME_TORSO
    transform       = [0.9489130973815918, 0.15944349765777588, 0.2722896933555603, 0.1422799825668335, -0.16740337014198303, 0.9858695864677429, 0.0060991644859313965, -0.20895415544509888, -0.2674696445465088, -0.051369789987802505, 0.9621959328651428, 0.020460091531276703, 0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63
#    axisMask   = motion.AXIS_MASK_VEL

    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
#    hit = -1
#    fractionMaxSpeed = 1
#          
#    motionProxy.changeAngles("RWristYaw", hit, fractionMaxSpeed)
#    time.sleep(0.04)
#        
#    motionProxy.setAngles("RWristYaw", -0.4, 1.0)
#        
#    time.sleep(0.5)
#    # motionProxy.changeAngles("RWristYaw", release, 1)        
#        
#    motionProxy.changeAngles("LWristYaw", -hit, fractionMaxSpeed)        
#    time.sleep(0.04)
#        
#    motionProxy.setAngles("LWristYaw", 0.4, 1.0)
#    # motionProxy.changeAngles("LWristYaw", -release, 1)        
#    time.sleep(0.5)
#
#    time.sleep(4.0)

#    # Go to rest position
#    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)