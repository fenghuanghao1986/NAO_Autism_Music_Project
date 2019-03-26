# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:53:15 2019

@author: CV_LAB_Howard
"""
# =============================================================================
# This is a find notes and hit template 
# =============================================================================
import almath
import random
import time
import argparse
import motion
from naoqi import ALProxy

# =============================================================================
# these notes is for temp use, later have to save them in one file and import
# =============================================================================
notes = {}
# Right Arm
notes[1] = [1.2180380821228027, -0.8589081192016602, 1.514016032218933, 
             0.6151759624481201, -0.7210218906402588, 0.22]

# note 2, 3, 4, 5 may have to re-do.
notes[2] = [1.2257080078125, -0.7538580417633057, 1.5094140768051147, 
             0.6427879333496094, -0.6719338893890381, 0.22]

notes[3] = [1.2011637687683105, -0.6551759624481201, 1.5078800916671753, 
             0.7563040256500244, -0.7609059810638428, 0.22]

notes[4] = [1.2011637687683105, -0.551759624481201, 1.5078800916671753, 
             0.7563040256500244, -0.7609059810638428, 0.22]

#notes[5] = [1.1029877662658691, -0.49859189987182617, 1.501744031906128, 
#           0.84527587890625, -0.9971418380737305, 0.22]
notes[5] = [1.12755947113037, -0.45325204849243164, 1.5109480619430542, 
             0.7977218627929688, -0.8698201179504395, 0.22]
# Left Arm
notes[6] = [0.9480281066894531, 0.3328361511230469, -1.512566089630127, 
             -0.7669579982757568, 1.2271580696105957, 0.22]

notes[7] = [1.0691561698913574, 0.5491299629211426, -1.4205260276794434, 
             -0.8053081035614014, 0.9617760181427002, 0.22]

notes[8] = [1.0568840503692627, 0.6581020545959473, -1.4220600128173828, 
             -0.8252501487731934, 0.9893879890441895, 0.22]

notes[9] = [1.1075060367584229, 0.7684919834136963, -1.4650120735168457, 
             -0.7915019989013672, 0.8482601642608643, 0.22]

notes[10] = [1.3207321166992188, 0.8283181190490723, -1.679771900177002, 
             -0.8620660305023193, 0.8682019710540771, 0.22]

notes[11] = [1.3529460430145264, 0.931096076965332, -1.679771900177002, 
             -0.7500841617584229, 0.7638900279998779, 0.22]

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
    
def userReadyToPlay(motionProxy, postureProxy):
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


def playXylo(motionProxy, keys, dt):
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.1)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.1)
             
            names = ['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand',
                     'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand']
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
                        note = list(notes[11])
                        if j == 4:
                            l.append(note[j])
                            l.append(note[j]+50*almath.TO_RAD)
                            l.append(note[j])
                        else:
                            l.append(note[j])
                            l.append(note[j])
                            l.append(note[j])
                    elif keys[k] == 3:
                        note = list(notes[7])
                        if j == 4:
                            l.append(note[j])
                            l.append(note[j]+50*almath.TO_RAD)
                            l.append(note[j])
                        else:
                            l.append(note[j])
                            l.append(note[j])
                            l.append(note[j])
                    elif keys[k] == 4:
                        note = list(notes[8])
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
                    elif keys[k] == 8:
                        note = list(notes[5])
                        if j == 4:
                            r.append(note[j])
                            r.append(note[j]-50*almath.TO_RAD)
                            r.append(note[j])
                        else:
                            r.append(note[j])
                            r.append(note[j])
                            r.append(note[j])
                    elif keys[k] == 9:
                        note = list(notes[4])
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
                            r.append(note[j]-50*almath.TO_RAD)
                            r.append(note[j])
                        else:
                            r.append(note[j])
                            r.append(note[j])
                            r.append(note[j])
                    elif keys[k] == 11:
                        note = list(notes[2])
                        if j == 4:
                            r.append(note[j])
                            r.append(note[j]-50*almath.TO_RAD)
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
                                note = list(notes[keys[nextk]])
                        r.append(note[j])
                        r.append(note[j])
                        r.append(note[j])
                        
                angleList.append(r)
                
            motionProxy.angleInterpolationBezier(names, timeList, angleList) 
            
# =============================================================================
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)  
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    postureProxy.goToPosture("Crouch", 0.4)
    userInitPosture(motionProxy, postureProxy)

    motionProxy.rest()
    
    while True:
        
        taskNumber = int(raw_input("select task:\n\
                                   1: test run\n\
                                   0: end\n\
                                   please make selection: "))
# =============================================================================
#       task 3: Start multiple notes play along with color
        if taskNumber == 1:
#            dt = 0.4
#            keys = [0,3,0,6,0,8,7,0,6,0,10,0,9,0,7,0,6,0,8,7,0,5,0,7,0,3,0,1,0,3]
#            dt = 0.6
#            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0,
#                    5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
#                    1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
#            dt = 0.5
#            keys = [0,0,5,6,7,5,5,6,7,5,7,8,9,0,7,8,9,0,
#                    9,10,9,8,7,5,9,10,9,8,7,5,
#                    5,2,5,0,5,2,5,0]   
#            dt = 0.6
#            keys = [1,3,0,5,7,9,0,2,4,6,0,8,10,11,0,2,5,8,0,4,7,0,11,3,4,0,5,7,8,9,0,1,10]
#            dt = 0.5
#            keys = [6,7,8,9,10,9,8,7,6,0,3,0,6,0,7,8,9,0,8,0,7,0,6,0,8,7,6,5,7,0,6,0,
#                    6,7,8,9,10,9,8,7,6,0,3,0,6,0,7,8,9,0,8,0,7,0,6,0,8,7,6,5,7,0,6,0]
            # never use lower than dt=0.4
            # Qing Hua Ci
#            dt = 0.4
#            keys = [0,2,1,6,1,0,1,6,1,0,1,6,1,6,5,0,0,2,1,6,1,0,1,6,1,0,1,3,2,1,1,0,0,5,6,3,
#                    3,0,3,2,3,0,3,2,3,5,0,3,0,3,3,3,2,2,2,2,2,0,1,3,0,0,0,0,0,2,1,6,1,0,1,6,
#                    1,0,1,6,1,6,5,0,0,5,6,3,5,0,5,3,5,0,5,3,2,1,1,0,0,2,1,2,3,2,2,0,2,0,1,6,
#                    2,1,1,6,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,3,2,3,4,0,2,3,5,3,2,0,0,0,
#                    0,5,5,3,2,3,5,0,2,3,5,2,1,0,0,0,0,1,2,3,5,6,5,4,5,3,3,2,2,0,0,0,0,1,2,1,
#                    1,0,1,2,0,3,0,5,0,3,0,0,0,5,5,3,2,3,6,0,2,3,5,3,2,0,0,0,0,5,5,3,2,3,5,0,
#                    2,3,5,2,1,0,0,0,0,1,2,3,5,6,5,4,5,3,3,2,2,0,0,5,3,0,2,2,0,1,0,0]

            # Girls like you
# =============================================================================
#            dt = 0.4
#            keys = [0,0,0,0,
#                     1,0,0,5,5,4,4,3,1,0,0,5,5,6,6,3,1,0,0,5,5,4,4,3,2,0,3,0,0,1,1,1,
#                     3,0,3,0,2,1,1,1,3,0,3,0,2,1,2,2,2,0,2,0,0,0,0,0,1,0,1,0,0,1,1,1,
#                     5,0,5,0,1,0,1,1,5,0,5,0,1,0,2,2,3,0,3,0,0,0,0,0,1,0,1,0,0,1,1,2,
#                     3,4,3,3,5,0,5,5,3,4,3,3,5,0,5,2,2,0,0,0,3,0,3,0,1,0,1,0,1,2,0,2,
#                     2,0,0,5,5,0,1,2,2,0,5,0,5,0,2,2,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,
#                     1,0,2,0,3,1,1,1,7,0,1,0,2,0,6,6,6,0,1,0,2,0,6,6,6,0,1,0,2,0,1,0]
# =============================================================================
            # let it go
            dt = 0.4
            keys = [0,0,0,0,
                    7,1,3,7,0,1,0,0,7,1,3,1,0,7,0,2,6,7,2,6,0,7,0,2,5,0,0,0,4,0,0,0,
                    7,1,3,7,0,1,0,0,1,7,3,1,0,7,0,2,6,7,2,6,0,7,0,2,5,0,0,0,4,0,0,0,
                    0,0,0,3,3,0,3,0,3,0,3,3,3,2,1,1,0,0,1,2,2,2,0,0,0,1,7,6,0,0,0,0,
                    0,0,0,3,3,3,3,3,0,3,5,5,3,3,0,0,0,0,2,2,2,3,0,0,0,2,1,2,0,2,0,0,
                    0,0,0,0,0,0,3,3,0,5,0,6,0,5,0,3,0,5,0,5,0,5,0,4,0,3,0,4,3,0,0,0,
                    0,0,0,0,0,0,3,3,2,1,0,2,0,0,3,3,2,0,1,0,0,0,6,0,0,0,0,0,0,0,0,0,
                    0,0,2,2,0,5,0,5,0,2,0,2,0,6,0,6,0,0,6,5,6,6,0,6,6,7,0,1,0,7,0,7,
                    0,0,2,2,0,5,0,5,0,0,2,2,0,6,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,
                    0,7,0,0,1,0,0,0,1,0,0,0,0,6,7,1,0,0,0,0,0,5,5,2,0,0,0,0,0,0,1,6,
                    6,6,6,0,6,7,0,1,0,0,0,0,0,6,7,1,0,0,0,0,0,5,3,3,3,2,0,0,0,1,2,3,
                    0,3,0,4,0,0,2,1,2,1,0,0,0,0,0,0,5,0,3,3,0,2,2,0,2,0,0,0,1,0,1,0,
                    5,5,0,3,0,1,1,0,1,0,0,0,0,0,1,1,7,0,5,5,0,0,5,0,5,0,0,0,0,0,0,4,
                    4,0,4,3,4,3,4,4,3,1,0,0,0,0,0,0]

            tts.say("play starts")
#            ledProxy.randomEyes(2.0)
        
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)
            playXylo(motionProxy, keys, dt)
            
            # since for 'R/LArm' has 6 angles invoved, so we have to assign
            # 6 interpolations for each of the joint
                      

            tts.say("Do you want to try it again?")
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            motionProxy.rest()   
            
# =============================================================================
# =============================================================================
#       task 9: end the session get out the loop
        elif taskNumber == 0:
            tts.say("Have a nice day! See you next time!")            
            motionProxy.rest()
            break
        
#       other typo or mistakes
        else:
            continue

# =============================================================================
# Calling the main
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
#    parser.add_argument("--ip", type=str, default="127.0.0.1",
#                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)    
# =============================================================================
# End of the test session program