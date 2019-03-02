# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:04:46 2019

@author: CV_LAB_Howard
"""
import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import argparse

class userContorl(AlModule):
    def __init__(self, name):
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
# =============================================================================
#    parser.add_argument("--ip", type=str, default="127.0.0.1",
#                         help="Robot ip address")
# =============================================================================
# =============================================================================
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                         help="Robot ip address")
# =============================================================================
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)