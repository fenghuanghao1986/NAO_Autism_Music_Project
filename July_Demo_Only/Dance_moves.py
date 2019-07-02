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

# left arm moves

moves[1] = [1.7134361267089844, 0.11961007118225098, -0.0015759468078613281, -0.03490658476948738, -1.5723919868469238, 1]

moves[2] = [1.672018051147461, 0.09046411514282227, 1.4894720315933228, -0.03490658476948738, -1.580061912536621, 1]

moves[3] = [1.6612800359725952, 1.2793140411376953, 0.08739614486694336, -0.038308143615722656, -1.5708580017089844, 1]

moves[4] = [1.6612800359725952, 1.2885180711746216, -0.04452800750732422, -1.4081701040267944, -1.580061912536621, 1]

moves[5] = [1.6612800359725952, 1.2701101303100586, -1.7135200500488281, -1.3928301334381104, -1.4803519248962402, 1]

moves[6] = [0.05518198013305664, -0.12429594993591309, -0.09054803848266602, -0.03490658476948738, -1.543245792388916, 1]

moves[7] = [0.05518198013305664, -0.15497589111328125, -0.08901405334472656, -1.4679961204528809, -1.5355758666992188, 1]

moves[8] = [0.05824995040893555, 1.2977221012115479, -0.05373191833496094, -0.03490658476948738, -1.5831298828125, 1]

moves[9] = [0.05824995040893555, 1.2915860414505005, -0.06753802299499512, -1.4112380743026733, -1.5938677787780762, 1]

moves[10] = [0.047512054443359375, 1.2869840860366821, -1.6721019744873047, -1.463394045829773, -1.392913818359375, 1]

# right arm moves

moves[11] = [1.7134361267089844, -0.11961007118225098, 0.0015759468078613281, 0.03490658476948738, -1.5723919868469238, 1]

moves[12] = [1.672018051147461, -0.09046411514282227, -1.4894720315933228, 0.03490658476948738, -1.580061912536621, 1]

moves[13] = [1.6612800359725952, -1.2793140411376953, -0.08739614486694336, 0.038308143615722656, -1.5708580017089844, 1]

moves[14] = [1.6612800359725952, -1.2885180711746216, 0.04452800750732422, 1.4081701040267944, -1.580061912536621, 1]

moves[15] = [1.6612800359725952, -1.2701101303100586, 1.7135200500488281, 1.3928301334381104, -1.4803519248962402, 1]

moves[16] = [0.05518198013305664, 0.12429594993591309, 0.09054803848266602, 0.03490658476948738, -1.543245792388916, 1]

moves[17] = [0.05518198013305664, 0.15497589111328125, 0.08901405334472656, 1.4679961204528809, -1.5355758666992188, 1]

moves[18] = [0.05824995040893555, -1.2977221012115479, 0.05373191833496094, 0.03490658476948738, -1.5831298828125, 1]

moves[19] = [0.05824995040893555, -1.2915860414505005, 0.06753802299499512, 1.4112380743026733, -1.5938677787780762, 1]

moves[20] = [0.047512054443359375, -1.2869840860366821, 1.6721019744873047, 1.463394045829773, -1.392913818359375, 1]

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