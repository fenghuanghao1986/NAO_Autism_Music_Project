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
import random
import argparse
from naoqi import ALProxy
#from naoqi import ALProxy

# =============================================================================
# these notes is for temp use, later have to save them in one file and import
# =============================================================================
moves = {}

# left arm moves

moves[1] = [1.7134361267089844, 0.11961007118225098, -0.0015759468078613281, 
             -0.03490658476948738, -1.5723919868469238, 1]

moves[2] = [1.672018051147461, 0.09046411514282227, 1.4894720315933228, 
             -0.03490658476948738, -1.580061912536621, 1]

moves[3] = [1.6612800359725952, 1.2793140411376953, 0.08739614486694336, 
             -0.038308143615722656, -1.5708580017089844, 1]

moves[4] = [1.6612800359725952, 1.2885180711746216, -0.04452800750732422, 
             -1.4081701040267944, -1.580061912536621, 1]

moves[5] = [1.6612800359725952, 1.2701101303100586, -1.7135200500488281, 
             -1.3928301334381104, -1.4803519248962402, 1]

moves[6] = [0.05518198013305664, -0.12429594993591309, -0.09054803848266602, 
             -0.03490658476948738, -1.543245792388916, 1]

moves[7] = [0.05518198013305664, -0.15497589111328125, -0.08901405334472656, 
             -1.4679961204528809, -1.5355758666992188, 1]

moves[8] = [0.05824995040893555, 1.2977221012115479, -0.05373191833496094, 
             -0.03490658476948738, -1.5831298828125, 1]

moves[9] = [0.05824995040893555, 1.2915860414505005, -0.06753802299499512, 
             -1.4112380743026733, -1.5938677787780762, 1]

moves[10] = [0.047512054443359375, 1.2869840860366821, -1.6721019744873047, 
             -1.463394045829773, -1.392913818359375, 1]

# right arm moves

moves[11] = [1.4723570346832275, -0.18541914224624634, 1.1937023401260376, 
     0.4103873670101166, 0.10000001639127731, 1]

moves[12] = [1.5060580968856812, -0.22906318306922913, -0.17627082765102386, 
     0.03490658476948738, 0.10000001639127731, 1]

moves[13] = [1.5707966089248657, -1.3124873638153076, 2.802596928649634e-45, 
     0.03490659222006798, 1.5707961320877075, 1]

moves[14] = [1.5707966089248657, -1.3124873638153076, 2.802596928649634e-45, 
     1.2095129489898682, 1.5707961320877075, 1]

moves[15] = [1.5707966089248657, -1.3124873638153076, 1.5707961320877075, 
     1.5446161031723022, 1.3124873638153076, 1]

moves[16] = [-2.802596928649634e-45, 2.802596928649634e-45, 2.802596928649634e-45, 
     0.03490658476948738, 1.5707966089248657, 1]

moves[17] = [2.802596928649634e-45, -1.326449990272522, -2.802596928649634e-45, 
     0.03490659222006798, 1.5707966089248657, 1]

moves[18] = [2.802596928649634e-45, -1.326449990272522, -2.802596928649634e-45, 
     1.5446161031723022, 1.5707966089248657, 1]

moves[19] = [2.802596928649634e-45, -1.326449990272522, 1.5707966089248657, 
     1.5446161031723022, 1.5707966089248657, 1]

moves[20] = [0.047512054443359375, -1.2869840860366821, 1.6721019744873047, 
             1.463394045829773, -1.392913818359375, 1]

# =============================================================================
# The following function initializes NAO's starting position or resting position
# =============================================================================
    
def userReadyToDance(postureProxy):

    postureProxy.goToPosture("StandZero", 0.5)
    
    time.sleep(2.0)

def Dance(motionProxy, keys, dt):
    
    motionProxy.setAngles("RArm", [0,0,0,0,0,0], 0.1)
    motionProxy.setAngles("LArm", [0,0,0,0,0,0], 0.1)
             
#    names = ['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand',
#             'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand']
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
            
            if keys[k] > 0 and keys[k] < 11: 
                note = list(moves[keys[k]])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+55*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
# ===========================================================================
            elif keys[k] == 11:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
            elif keys[k] == 12:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
            elif keys[k] == 13:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
            elif keys[k] == 14:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
            elif keys[k] == 15:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
            elif keys[k] == 16:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
            elif keys[k] == 17:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
            elif keys[k] == 18:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
                    
            elif keys[k] == 19:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
            elif keys[k] == 20:
                note = list(moves[random.randint(1,10)])
                if j == 4:
                    l.append(note[j])
                    l.append(note[j]+50*almath.TO_RAD)
                    l.append(note[j])
                else:
                    l.append(note[j])
                    l.append(note[j])
                    l.append(note[j])
            else:
                l.append(note[j])
                l.append(note[j])
                l.append(note[j])
                        
        angleList.append(l)
# =============================================================================
#             
# =============================================================================
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
            
            if keys[k] > 10 and keys[k] < 21: 
                note = list(moves[keys[k]])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-55*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
# ============================================================================
            elif keys[k] == 1:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-50*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            elif keys[k] == 2:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-50*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            elif keys[k] == 3:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-40*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            elif keys[k] == 4:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-45*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            elif keys[k] == 5:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-50*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            elif keys[k] == 6:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-50*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            elif keys[k] == 7:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-40*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            elif keys[k] == 8:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-45*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            elif keys[k] == 9:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-40*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            elif keys[k] == 10:
                note = list(moves[random.randint(11,20)])
                if j == 4:
                    r.append(note[j])
                    r.append(note[j]-45*almath.TO_RAD)
                    r.append(note[j])
                else:
                    r.append(note[j])
                    r.append(note[j])
                    r.append(note[j])
            else:
                 r.append(note[j])
                 r.append(note[j])
                 r.append(note[j])
                        
        angleList.append(r)
    print(len(armNames))
    print(len(timeList)) 
    print(len(angleList)) 
    motionProxy.angleInterpolationBezier(armNames, timeList, angleList)
    
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)  
#    ledProxy = ALProxy("ALLeds", robotIP, PORT)
#    tts = ALProxy("ALTextToSpeech", robotIsP, PORT)
#    userReadyToDance(postureProxy)
    dt = 0.83
#    dt = 2
    keys = []
    for i in range(0, 20):
        keys.append(random.randint(0, 20))
    print(keys)
#    keys = [11,12,13,14,15,16,17,18,19,20]
    Dance(motionProxy, keys, dt)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=51677,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)