# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:46:17 2019

@author: CV_LAB_Howard
"""

global armNames; armNames = ['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand',
                             'LHipYawPitch',  'LHipRoll', 'LHipPitch', 'LKneePitch', 'LAnklePitch', 'LAnkleRoll',
                             'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand',
                             'RHipYawPitch', 'RHipRoll', 'RHipPitch', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll']

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

moves[12] = [0.4432840347290039, 0.07972598075866699, -0.8207318782806396, -1.5446163415908813, -0.09361600875854492, 0,
             -0.17023205757141113, 0.09975194931030273, 0.1304318904876709, -0.09054803848266602, 0.09046411514282227, -0.13034796714782715]
moves[13] = [0.7746281623840332, -0.03992605209350586, -0.7578380107879639, -1.5446163415908813, 0.37272000312805176, 0,
             -0.4494199752807617, 0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, -0.16409611701965332]
moves[14] = [0.6565101146697998, -0.3141592741012573, -0.038392066955566406, -1.142788052558899, 0.5828781127929688, 0,
             -0.17023205757141113, 0.09975194931030273, 0.1304318904876709, -0.09054803848266602, 0.09046411514282227, -0.13034796714782715]
moves[15] = [0.6565101146697998, -0.3141592741012573, -0.038392066955566406, -1.142788052558899, 0.5828781127929688, 0,
             -0.4494199752807617, 0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, -0.16409611701965332]
moves[16] = [0.03984212875366211, -0.3141592741012573, -0.15804386138916016, -0.9602420330047607, -1.5831298828125, 0,
             -0.17023205757141113, 0.09975194931030273, 0.1304318904876709, -0.09054803848266602, 0.09046411514282227, -0.13034796714782715]
moves[17] = [0.6657140254974365, -0.3141592741012573, -0.06600403785705566, -1.1504580974578857, -1.0692400932312012, 0,
             -0.4494199752807617, 0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, -0.16409611701965332]
moves[18] = [0.21778607368469238, -0.04606199264526367, -0.6980118751525879, -1.5446163415908813, -0.14270401000976562, 0,
             -0.17023205757141113, 0.09975194931030273, 0.1304318904876709, -0.09054803848266602, 0.09046411514282227, -0.13034796714782715]
moves[19] = [0.0827939510345459, -0.3141592741012573, -0.15804386138916016, -1.4342480897903442, -0.05373191833496094, 0,
             -0.4494199752807617, 0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, -0.16409611701965332]
moves[20] = [0.07972598075866699, -0.12276196479797363, -1.7104520797729492, -1.515550136566162, -4.1961669921875e-05, 0,
             -0.17023205757141113, 0.09975194931030273, 0.1304318904876709, -0.09054803848266602, 0.09046411514282227, -0.13034796714782715]
moves[21] = [0.07972598075866699, -0.12276196479797363, -1.7104520797729492, -1.515550136566162, -4.1961669921875e-05, 0,
             -0.4494199752807617, 0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, -0.16409611701965332]
moves[22] = [0.12727999687194824, -0.3141592741012573, -0.18719005584716797, -1.4618600606918335, -0.06447005271911621, 0,
             -0.17023205757141113, 0.09975194931030273, 0.1304318904876709, -0.09054803848266602, 0.09046411514282227, -0.13034796714782715]

# right arm moves

moves[1] = [0.43416404724121094, -0.06907200813293457, 0.7761621475219727, 1.5446163415908813, 0.12114405632019043, 0,
            -0.17023205757141113, -0.09966802597045898, 0.13034796714782715, -0.09046411514282227, 0.09054803848266602, 0.1304318904876709]
moves[2] = [0.2715599536895752, -0.042994022369384766, 0.6457719802856445, 1.5446163415908813, 0.25, 0,
            -0.4494199752807617, -0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, 0.16409611701965332]
moves[3] = [0.06753802299499512, 0.3141592741012573, 0.16563010215759277, 1.489555835723877, 0.10426998138427734, 0,
            -0.17023205757141113, -0.09966802597045898, 0.13034796714782715, -0.09046411514282227, 0.09054803848266602, 0.1304318904876709]
moves[4] = [0.2454819679260254, 0.11961007118225098, 1.5769100189208984, 1.5033621788024902, -0.04912996292114258, 0,
            -0.4494199752807617, -0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, 0.16409611701965332]
moves[5] = [0.2454819679260254, 0.11961007118225098, 1.5769100189208984, 1.5033621788024902, -0.04912996292114258, 0,
            -0.17023205757141113, -0.09966802597045898, 0.13034796714782715, -0.09046411514282227, 0.09054803848266602, 0.1304318904876709]
moves[6] = [0.14577198028564453, 0.3141592741012573, 0.09966802597045898, 1.4251279830932617, 0.07819199562072754, 0,
            -0.4494199752807617, -0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, 0.16409611701965332]
moves[7] = [0.5676219463348389, -0.08748006820678711, 0.5844120979309082, 1.5446163415908813, 0.019900083541870117, 0,
            -0.17023205757141113, -0.09966802597045898, 0.13034796714782715, -0.09046411514282227, 0.09054803848266602, 0.1304318904876709]
moves[8] = [0.5706899166107178, 0.3141592741012573, -0.0353238582611084, 1.1950278282165527, -0.31297802925109863, 0,
            -0.4494199752807617, -0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, 0.16409611701965332]
moves[9] = [0.5706899166107178, 0.3141592741012573, -0.0353238582611084, 1.1950278282165527, -0.31297802925109863, 0,
            -0.17023205757141113, -0.09966802597045898, 0.13034796714782715, -0.09046411514282227, 0.09054803848266602, 0.1304318904876709]
moves[10] = [-0.0030260086059570312, 0.3141592741012573, 0.047512054443359375, 0.9725980758666992, 1.6873581409454346, 0,
             -0.4494199752807617, -0.26695799827575684, -0.4893040657043457, 1.5247540473937988, -0.6335840225219727, 0.16409611701965332]
moves[11] = [0.6703999042510986, 0.30062198638916016, 0.07052206993103027, 1.2717280387878418, 1.0890979766845703, 0,
             -0.17023205757141113, -0.09966802597045898, 0.13034796714782715, -0.09046411514282227, 0.09054803848266602, 0.1304318904876709]

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
    
    for h in range(12):
        t = []
        for i in range(len(keys)): 
            
            t.append(dt*(i+1))
            t.append(dt*(i+1) + 0.1)
            
        timeList.append(t)   
            
    for j in range(12):
        l = []                
        for k in range(len(keys)):
            
            if keys[k] > 11 and keys[k] < 23: 
                note = list(moves[keys[k]])
                l.append(note[j])
                l.append(note[j])
# ===========================================================================
            elif keys[k] == 1:
                note = list(moves[12])
                l.append(note[j])
                l.append(note[j])
            elif keys[k] == 2:
                note = list(moves[13])
                l.append(note[j])
                l.append(note[j])
            elif keys[k] == 3:
                note = list(moves[14])
                l.append(note[j])
                l.append(note[j])
            elif keys[k] == 4:
                note = list(moves[15])
                l.append(note[j])
                l.append(note[j])
            elif keys[k] == 5:
                note = list(moves[16])
                l.append(note[j])
                l.append(note[j])
            elif keys[k] == 6:
                note = list(moves[17])
                l.append(note[j])
                l.append(note[j])
            elif keys[k] == 7:
                note = list(moves[18])
                l.append(note[j])
                l.append(note[j])
            elif keys[k] == 8:
                note = list(moves[19])
                l.append(note[j])
                l.append(note[j])                    
            elif keys[k] == 9:
                note = list(moves[20])
                l.append(note[j])
                l.append(note[j])
            elif keys[k] == 10:
                note = list(moves[21])
                l.append(note[j])
                l.append(note[j])
            elif keys[k] == 11:
                note = list(moves[22])
                l.append(note[j])
                l.append(note[j])
            else:
                l.append(note[j])
                l.append(note[j])
                        
        angleList.append(l)
# =============================================================================
#             
# =============================================================================
    for h in range(12):
        t = []
        for i in range(len(keys)): 
            
            t.append(dt*(i+1))
            t.append(dt*(i+1) + 0.1)
            
        timeList.append(t)    
            
    for j in range(12):
        r = []                
        for k in range(len(keys)):
            
            if keys[k] > 0 and keys[k] < 12: 
                note = list(moves[keys[k]])
                r.append(note[j])
                r.append(note[j])
# ============================================================================
            elif keys[k] == 12:
                note = list(moves[1])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 13:
                note = list(moves[2])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 14:
                note = list(moves[3])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 15:
                note = list(moves[4])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 16:
                note = list(moves[5])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 17:
                note = list(moves[6])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 18:
                note = list(moves[7])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 19:
                note = list(moves[8])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 20:
                note = list(moves[9])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 21:
                note = list(moves[10])
                r.append(note[j])
                r.append(note[j])
            elif keys[k] == 22:
                note = list(moves[11])
                r.append(note[j])
                r.append(note[j])
            else:
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
    userReadyToDance(postureProxy)
    dt = 0.5
#    dt = 2
#    keys = []
#    for i in range(0, 22):
#        keys.append(random.randint(0, 22))
#    print(keys)
    keys = [1,2,3,4,5,6,1,7,8,9,10,11,1,
            12,13,14,15,16,17,12,18,19,20,21,22,12]
    Dance(motionProxy, keys, dt)
    userReadyToDance(postureProxy)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)