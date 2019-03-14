# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:40:02 2019

@author: CV_LAB_Howard
"""

# =============================================================================
# This is a LED test code
# =============================================================================

import sys
from naoqi import ALProxy
robotIP = '127.0.0.1'
PORT = 9559
# Example showing how to switch on a group
ledProxy = ALProxy("ALLeds", robotIP, PORT)
name = 'LeftFaceLeds'
colorName = 'red'
#name = 'RightFaceLeds'
#colorName = 'green'
#name = 'ChestLeds'
#colorName = 'blue'
duration = 2.0
ledProxy.fadeRGB(name, colorName, duration)
sys.exit(0)