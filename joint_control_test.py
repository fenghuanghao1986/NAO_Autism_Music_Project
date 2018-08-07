# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:48:21 2018

@author: CV_LAB_Howard
"""

import time
import argparse
from naoqi import ALProxy

def main(robotIP, PORT = 9559):
    motionProxy = ALProxy("ALMotion", robotIP, PORT)

    motionProxy.setStiffnesses("LArm", 1.0)

    # Example showing a slow, relative move of "HeadYaw".
    # Calling this multiple times will move the head further.
    names = "LWristYaw"
    hit = 0.3
    release = -0.3
    fractionMaxSpeed = 1
    motionProxy.changeAngles(names, hit, fractionMaxSpeed)
    
    time.sleep(0.2)
    
    motionProxy.changeAngles(names, release, fractionMaxSpeed)

    time.sleep(2.0)

    motionProxy.setStiffnesses("LArm", 0.0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)