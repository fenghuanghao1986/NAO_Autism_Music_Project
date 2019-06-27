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

    transform       = [0.4127737283706665, -0.21474865078926086, -0.8851559162139893, 
                       0.06692149490118027, -0.907514750957489, -0.17985010147094727, 
                       -0.37956666946411133, -0.29789382219314575, -0.0776839479804039, 
                       0.9599671959877014, -0.26912495493888855, 0.06466364860534668, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, 
                              fractionMaxSpeed, axisMask)
        
    chainName        = "LArm"
    frame            = motion.FRAME_TORSO

    transform       = [0.3653983175754547, 0.20093390345573425, -0.9089057445526123, 
                       0.056045692414045334, 0.911535382270813, -0.2751205563545227, 
                       0.30563390254974365, 0.29891785979270935, -0.18864643573760986, 
                       -0.940177857875824, -0.28368696570396423, 0.04994587600231171, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, 
                              fractionMaxSpeed, axisMask)
    

    time.sleep(2.0)


def Dance(motionProxy, keys, dt):
            motionProxy.setAngles("RArm", 
                                  [0,0,0,0,0,0], 
                                   0.1)
            motionProxy.setAngles("LArm", 
                                  [0,0,0,0,0,0], 
                                   0.1)
             

            # tempo
            timeList = []
            angleList = []
            for h in range(6):
                t = []
                for i in range(len(keys)): 
                    
                    t.append(dt*(i+1))
                    t.append(dt*(i+1) + 0.07)
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
# =============================================================================
                    elif keys[k] == 1:
                         note = list(notes[10])
                         if j == 4:
                             l.append(note[j])
                             l.append(note[j]+50*almath.TO_RAD)
                             l.append(note[j])
                         else:
                             l.append(note[j])
                             l.append(note[j])
                             l.append(note[j])
                    elif keys[k] == 2:
                         note = list(notes[6])
                         if j == 4:
                             l.append(note[j])
                             l.append(note[j]+50*almath.TO_RAD)
                             l.append(note[j])
                         else:
                             l.append(note[j])
                             l.append(note[j])
                             l.append(note[j])
                    elif keys[k] == 3:
                         note = list(notes[8])
                         if j == 4:
                             l.append(note[j])
                             l.append(note[j]+50*almath.TO_RAD)
                             l.append(note[j])
                         else:
                             l.append(note[j])
                             l.append(note[j])
                             l.append(note[j])
                    elif keys[k] == 4:
                         note = list(notes[9])
                         if j == 4:
                             l.append(note[j])
                             l.append(note[j]+50*almath.TO_RAD)
                             l.append(note[j])
                         else:
                             l.append(note[j])
                             l.append(note[j])
                             l.append(note[j])
                    else:
                         note = list(notes[8])
                         if k != len(keys)-1:
                             nextk = k
                             for x in range(k+1, len(keys)):
                                 if keys[x] > 5 and keys[x] < 12:
                                     nextk = x
                                     break 
                             if nextk != k:
                                 note = list(notes[keys[nextk]])
                         l.append(note[j])
                         l.append(note[j])
                         l.append(note[j])
# =============================================================================
                        
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
# =============================================================================
                    elif keys[k] == 8:
                         note = list(notes[3])
                         if j == 4:
                             r.append(note[j])
                             r.append(note[j]-50*almath.TO_RAD)
                             r.append(note[j])
                         else:
                             r.append(note[j])
                             r.append(note[j])
                             r.append(note[j])
                    elif keys[k] == 9:
                         note = list(notes[5])
                         if j == 4:
                             r.append(note[j])
                             r.append(note[j]-50*almath.TO_RAD)
                             r.append(note[j])
                         else:
                             r.append(note[j])
                             r.append(note[j])
                             r.append(note[j])
                    elif keys[k] == 10:
                         note = list(notes[1])
                         if j == 4:
                             r.append(note[j])
                             r.append(note[j]-40*almath.TO_RAD)
                             r.append(note[j])
                         else:
                             r.append(note[j])
                             r.append(note[j])
                             r.append(note[j])
                    elif keys[k] == 11:
                         note = list(notes[2])
                         if j == 4:
                             r.append(note[j])
                             r.append(note[j]-45*almath.TO_RAD)
                             r.append(note[j])
                         else:
                             r.append(note[j])
                             r.append(note[j])
                             r.append(note[j])
                    else:
                         note = list(notes[3])
                         if k != len(keys)-1:
                             nextk = k
                             for x in range(k+1, len(keys)):
                                 if keys[x] != 0 and keys[x] > 0 and keys[x] < 6:
                                     nextk = x
                                     break
                             if nextk != k:
                                 note = list(moves[keys[nextk]])
                         r.append(note[j])
                         r.append(note[j])
                         r.append(note[j])
# =============================================================================
                        
                angleList.append(r)
                
            motionProxy.angleInterpolationBezier(armNames, timeList, angleList)
            
# =============================================================================