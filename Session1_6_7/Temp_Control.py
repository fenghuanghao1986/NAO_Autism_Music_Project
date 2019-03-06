# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:47:17 2019

@author: fengh
"""

# This fucntion is to have tempreture control
# in case some of the motors getting too hot
# casuing program failure

import almath
import time
import motion
import argparse
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

def tempControl():
    