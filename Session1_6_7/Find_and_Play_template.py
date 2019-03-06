# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:53:15 2019

@author: CV_LAB_Howard
"""

# =============================================================================
# This is a find notes and hit template 
# =============================================================================
import almath
import time
import argparse
from naoqi import ALProxy
# =============================================================================
# these notes is for temp use, later have to save them in one file and import
# =============================================================================
notes = {}
# Right Arm
notes['1'] = []     #C6
notes['2'] = []     #D6
notes['3'] = []     #E6
notes['4'] = []     #F6
notes['5'] = []     #G6
# Left Arm
notes['6'] = []     #A6
notes['7'] = []     #B6
notes['8'] = []     #C7
notes['9'] = []     #D7
notes['10'] = []    #E7
notes['11'] = []    #F7
# =============================================================================
# 
# =============================================================================
def playXylophone(motionProxy, notes):
    # input notes is dictionary type, including key as note, and 
    # values as set of angles
    # anglse related to hit will be a seperate list
    for key in range(notes.keys()):        
        # identify which hand to use to find and hit current note
        if key > 0 and key < 6:
            
            names = ['RArm', 'RWristYaw']
            
            current_note = motionProxy.getAngles(names[0])
            target_note = list(notes[key])
            beforeHit = motionProxy.getAngles(names[1])
            onHit = beforeHit + 30*almath.TO_RAD
            afterHit = beforeHit
            
            angleLists = [[current_note], [target_note],
                          [beforeHit, onHit, afterHit]]
            
            timeLists  = [[0.1, 0.6], [0.01, 0.05, 0.08]]
            
            motionProxy.angleInterpolationBezier(names, timeLists, angleLists)
            
            time.sleep(0.2)
        else:
            
            names = ['LArm', 'LWristYaw']
            
            current_note = motionProxy.getAngles(names[0])
            target_note = list(notes[key])
            beforeHit = motionProxy.getAngles(names[1])
            onHit = beforeHit + 30*almath.TO_RAD
            afterHit = beforeHit
                
            angleLists = [[current_note], [target_note],
                          [beforeHit, onHit, afterHit]]
            
            timeLists  = [[0.1, 0.6], [0.01, 0.05, 0.08]]
            
            motionProxy.angleInterpolationBezier(names, timeLists, angleLists)
            
            time.sleep(0.2)           
# =============================================================================
# 
# =============================================================================
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    playXylophone(motionProxy)
# =============================================================================
# 
# =============================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)