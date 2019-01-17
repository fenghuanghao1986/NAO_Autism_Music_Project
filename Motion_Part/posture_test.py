# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 10:46:02 2018

@author: CV_LAB_Howard
"""

import sys
import time

from naoqi import ALProxy


def main(robotIP):

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    postureProxy.goToPosture("StandInit", 1.0)
    time.sleep(1)
    postureProxy.goToPosture("SitRelax", 1.0)
    time.sleep(1)
    postureProxy.goToPosture("StandZero", 1.0)
    time.sleep(1)
#    postureProxy.goToPosture("LyingBelly", 1.0)
#    time.sleep(1)
#    postureProxy.goToPosture("LyingBack", 1.0)
    time.sleep(1)
    postureProxy.goToPosture("Stand", 1.0)
    time.sleep(1)
    postureProxy.goToPosture("Crouch", 1.0)
    time.sleep(1)
#    postureProxy.goToPosture("Sit", 1.0)
#    time.sleep(1)

    print postureProxy.getPostureFamily()


if __name__ == "__main__":
    robotIp = "127.0.0.1"

    if len(sys.argv) <= 1:
        print "Usage python alrobotposture.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)