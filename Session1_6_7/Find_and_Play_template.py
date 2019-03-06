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
notes[1] = []     #C6
notes[2] = []     #D6
notes[3] = []     #E6
notes[4] = []     #F6
notes[5] = []     #G6
# Left Arm
notes[6] = [0.6902580261230469, 0.7255401611328125, -1.4634780883789062, -0.6795201301574707, 0.9955241680145264, 0.23240000009536743]     #A6
notes[7] = [0.7055981159210205, 0.15949392318725586, -1.2978057861328125, -0.6810541152954102, 1.2072160243988037, 0.23240000009536743]     #B6
notes[8] = [0.556800127029419, 0.3128941059112549, -1.2978057861328125, -0.6994619369506836, 1.0921659469604492, 0.23240000009536743]     #C7
notes[9] = [0.5614020824432373, 0.6902580261230469, -1.299339771270752, -0.6994619369506836, 0.9080860614776611, 0.23240000009536743]     #D7
notes[10] = [0.5828781127929688, 0.9464361667633057, -1.2901358604431152, -0.6319661140441895, 0.7822980880737305, 0.23240000009536743]    #E7
notes[11] = [0.6703159809112549, 1.236362099647522, -1.5708580017089844, -0.3451080322265625, 0.7991721630096436, 0.23240000009536743]    #F7
# =============================================================================
# 
# =============================================================================
def playXylophone(motionProxy, keys):
    # input notes is dictionary type, including key as note, and 
    # values as set of angles
    # anglse related to hit will be a seperate list
    motionProxy.setStiffnesses("Body", 0)
    
    motionProxy.setStiffnesses("LArm", 1)
    motionProxy.setStiffnesses("RArm", 1)
    
    for key in keys:        
        # identify which hand to use to find and hit current note
        if key > 0 and key < 6:
            
            names = ['RArm', 'RWristYaw']
            useSensors  = True
            
            current_note = motionProxy.getAngles(names[0], useSensors)
            target_note = list(notes[key])
            beforeHit = motionProxy.getAngles(names[1], useSensors)
            onHit = beforeHit[0] + 90*almath.TO_RAD
            afterHit = beforeHit
            
            angleLists = [[current_note[0], target_note[0]], 
                          [current_note[1], target_note[1]],
                          [current_note[2], target_note[2]],
                          [current_note[3], target_note[3]],
                          [current_note[4], target_note[4]],
                          [current_note[5], target_note[5]],
                          [beforeHit[0], onHit, afterHit[0]]]
            
            timeLists  = [[0.1, 0.9], 
                          [0.1, 0.9],
                          [0.1, 0.9],
                          [0.1, 0.9],
                          [0.1, 0.9],
                          [0.1, 0.9],
                          [0.04, 0.08, 0.1]]
            
            motionProxy.angleInterpolationBezier(names, timeLists, angleLists)
            
            time.sleep(0.2)
        else:
            
            names = ['LArm', 'LWristYaw']
            useSensors  = True
            
            current_note = motionProxy.getAngles(names[0], useSensors)
            target_note = list(notes[key])
            beforeHit = motionProxy.getAngles(names[1], useSensors)
            onHit = beforeHit[0] + 90*almath.TO_RAD
            afterHit = beforeHit
                
            angleLists = [[current_note[0], target_note[0]], 
                          [current_note[1], target_note[1]],
                          [current_note[2], target_note[2]],
                          [current_note[3], target_note[3]],
                          [current_note[4], target_note[4]],
                          [current_note[5], target_note[5]],
                          [beforeHit[0], onHit, afterHit[0]]]
            
            timeLists  = [[0.1, 0.9], 
                          [0.1, 0.9],
                          [0.1, 0.9],
                          [0.1, 0.9],
                          [0.1, 0.9],
                          [0.1, 0.9],
                          [0.04, 0.08, 0.1]]
            
            motionProxy.angleInterpolationBezier(names, timeLists, angleLists)
            
            time.sleep(0.2)           
# =============================================================================
# 
# =============================================================================
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    keys = [6,8,7,11,9,8,7,10,6,8,6,10]
    playXylophone(motionProxy, keys)
# =============================================================================
# 
# =============================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.3",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)