# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:17:30 2019

@author: CV_LAB_Howard
"""
global armNames; armNames = ['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand',
                             'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand']
global legNames; legNames = ['LHipYawPitch',  'LHipRoll', 'LHipPitch', 'LKneePitch', 'LAnklePitch', 'LAnkleRoll',
                             'RHipRoll', 'RHipPitch', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll']

import almath
import time
import motion
#from naoqi import ALProxy

# =============================================================================
# these notes is for temp use, later have to save them in one file and import
# =============================================================================
moves = {}

moves[1] = []

moves[2] = []

moves[3] = []

moves[4] = []

moves[5] = []

moves[6] = []

moves[7] = []

moves[8] = []

moves[9] = []

moves[10] = []

moves[11] = []

moves[12] = []

# =============================================================================
# The following function initializes NAO's starting position or resting position
# =============================================================================
def userInitPosture(motionProxy, postureProxy):
# =============================================================================
#     # this function should have NAO crouching position with leg joints rest/locked?
#     # and both arms should be straight down without touching legs and other parts
# =============================================================================
    motionProxy.setStiffnesses("LArm", 1)
    motionProxy.setStiffnesses("RArm", 1)
    
    names  = ["LHipYawPitch", "LHipPitch", "RHipPitch"]
    angles  = [-0.25, -0.7, -0.7]
    fractionMaxSpeed  = 0.1
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    motionProxy.setStiffnesses("LHipYawPitch", 0.2)
    motionProxy.setStiffnesses("LHipPitch", 0.2)
    motionProxy.setStiffnesses("RHipPitch", 0.2)
    motionProxy.setStiffnesses("LLeg", 0.2)
    motionProxy.setStiffnesses("RLeg", 0.2)
    
    chainName        = "RArm"
    frame            = motion.FRAME_TORSO

    transform       = [0.035065650939941406, 0.18206071853637695, -0.9826618432998657, 
                       0.01609862968325615, -0.38233551383018494, -0.9060218334197998, 
                       -0.1815047711133957, -0.1932658553123474, -0.9233579635620117, 
                       0.3820711076259613, 0.03783803433179855, -0.09672538936138153, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, 
                              fractionMaxSpeed, axisMask)
    
    chainName        = "LArm"
    frame            = motion.FRAME_TORSO

    transform       = [0.03785611316561699, -0.17644673585891724, -0.9835819602012634, 
                       0.016386376693844795, 0.37893712520599365, -0.9082373380661011, 
                       0.17751504480838776, 0.19260691106319427, -0.9246478080749512, 
                       -0.3794357478618622, 0.03247988224029541, -0.09699571877717972, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, 
                              fractionMaxSpeed, axisMask)
    
    time.sleep(2.0)
    
def userReadyToDance(motionProxy, postureProxy):
# =============================================================================
# Have to record the transformation for ready to play position
# =============================================================================
    motionProxy.setStiffnesses("LArm", 1)
    motionProxy.setStiffnesses("RArm", 1)
    motionProxy.setSitffnesses("RLeg", 1)
    motionProxy.setSitffnesses("LLeg", 1)
    
    names  = ["LHipYawPitch", "LHipPitch", "RHipPitch"]
    angles  = [-0.25, -0.7, -0.7]
    fractionMaxSpeed  = 0.1
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    
    postureProxy.goToPosture("StandZero", 0.5)
    
    time.sleep(2.0)

def Dance(motionProxy, keys, dt):
    
    motionProxy.setAngles("RArm", [0,0,0,0,0,0], 0.1)
    motionProxy.setAngles("LArm", [0,0,0,0,0,0], 0.1)
             
    timeList = []
    angleList = []
    
    # generate a time list for all 12 joints for both arms 
    for h in range (12):
        t = []
        for i in range(len(keys)):
            t.append(dt*(i+1))
            t.append(dt*(i+1) + 0.1)
        
        timeList.append(t)
    
             
            for j in range(6):
                l = []                
                for k in range(len(keys)):
                            
                    if keys[k] > 5 and keys[k] < 12: 
                        note = list(notes[keys[k]])
                        if j == 4:
                            l.append(note[j])
                            l.append(note[j]+55*almath.TO_RAD)
                            l.append(note[j])
                        else:
                            l.append(note[j])
                            l.append(note[j])
                            l.append(note[j])

                angleList.append(l)
            
            for h in range(6):
                t = []
                for i in range(len(keys)): 
                    
                    t.append(dt*(i+1))
                    t.append(dt*(i+1) + 0.07)
                    t.append(dt*(i+1) + 0.1)
                        
                timeList.append(t)    
            
            for j in range(6):
                r = []                
                for k in range(len(keys)):
                            
                    if keys[k] > 0 and keys[k] < 6: 
                        note = list(notes[keys[k]])
                        if j == 4:
                            r.append(note[j])
                            r.append(note[j]-55*almath.TO_RAD)
                            r.append(note[j])
                        else:
                            r.append(note[j])
                            r.append(note[j])
                            r.append(note[j])

                        
                angleList.append(r)
                
            motionProxy.angleInterpolationBezier(armNames, timeList, angleList)
            
# =============================================================================