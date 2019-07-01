# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 12:58:55 2019

@author: fengh
"""

import almath
import time
import argparse
from naoqi import ALProxy

def main(robotIP, PORT = 9559):
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    motionProxy.setStiffnesses("LArm", 1.0)

    # Example showing multiple trajectories
    names      = ['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 
                  'LElbowRoll', 'LWristYaw', 'LHand']
    angleLists = [[-90.0*almath.TO_RAD, 0.0*almath.TO_RAD, 90.0*almath.TO_RAD], 
                  [10.0*almath.TO_RAD, 76.0*almath.TO_RAD],
                  [90.0*almath.TO_RAD, 0.0*almath.TO_RAD, -90.0*almath.TO_RAD],
                  [-2.0*almath.TO_RAD, -88.0*almath.TO_RAD, -2.0*almath.TO_RAD],
                  [90.0*almath.TO_RAD, 0.0*almath.TO_RAD, -90.0*almath.TO_RAD],
                  [1, 0, 1]]
    timeLists  = [[0.5, 1.0, 1.5], 
                  [2.0, 2.5],
                  [3.0, 3.5, 4.0],
                  [4.5, 5.0, 5.5],
                  [6.0, 6.5, 7.0],
                  [7.5, 8.0, 8.5]]
    motionProxy.angleInterpolationBezier(names, timeLists, angleLists)
    postureProxy.goToPosture("StandZero", 0.5)

    motionProxy.setStiffnesses("LArm", 0.0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=57008,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)