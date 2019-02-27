# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:08:33 2019

@author: CV_LAB_Howard
"""

import time
import motion
import argparse
from naoqi import ALProxy

def userInitPosture(motionProxy, postureProxy):
    
    # this function should have NAO crouching position with leg joints rest/locked?
    # and both arms should be straight down without touching legs and other parts
     
    postureProxy.goToPosture("Crouch", 0.5)
    time.sleep(1)
    
    chainName        = "RArm"
    frame            = motion.FRAME_TORSO
#    transform        = [1.0, 0.0, 0.0, 0.00,
#                        0.0, 1.0, 0.0, 0.00,
#                        0.0, 0.0, 1.0, 0.25]
    transform       = [0.03477038815617561, 0.9961863160133362, 0.080023854970932, 
                       0.0029639352578669786, -0.381715327501297, 0.0872393399477005, 
                       -0.9201536178588867, -0.183818519115448, -0.923625648021698, 
                       0.0014477664371952415, 0.38329294323921204, -0.10117591917514801, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation
#    axisMask   = motion.AXIS_MASK_VEL
#    print(motion.AXIS_MASK_VEL)
    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    chainName        = "LArm"
    frame            = motion.FRAME_TORSO
#    transform        = [1.0, 0.0, 0.0, 0.00,
#                        0.0, 1.0, 0.0, 0.00,
#                        0.0, 0.0, 1.0, 0.25]
    transform       = [0.03795033320784569, -0.9755989909172058, -0.21625538170337677, 
                       0.006952085066586733, 0.378103643655777, -0.1863023042678833, 
                       0.9068236947059631, 0.18319708108901978, -0.9249851703643799, 
                       -0.11618120968341827, 0.36180728673934937, -0.10128530114889145, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation
#    axisMask   = motion.AXIS_MASK_VEL
#    print(motion.AXIS_MASK_VEL)
    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    motionProxy.setStiffnesses("LLeg", 0.0)
    motionProxy.setStiffnesses("RLeg", 0.0)
    
    
    
# C = 1; D = 2; E = 3; F = 4; G = 5; A = 6; H = 7; C_2 = 8; D_2 = 9; E_2 = 10; F_2 = 11; 
def userSetTransform(motionProxy, key):

#    # Wake up robot
#    motionProxy.wakeUp()
#
#    # Send robot to Pose Init
#    postureProxy.goToPosture("StandInit", 0.5)

#    time.sleep(4.0)
    # Example showing how to set Torso Transform, using a fraction of max speed

    motionProxy.setStiffnesses("LArm", 1.0)
    motionProxy.setStiffnesses("RArm", 1.0)
    
    
    #Red
    if (key==3):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9422568678855896, 0.2736080288887024, 0.19310784339904785, 0.1298113465309143, -0.29820317029953003, 0.947908341884613, 0.11200278997421265, -0.21574079990386963, -0.15240366756916046, -0.16312076151371002, 0.9747639298439026, 0.008839884772896767, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63 # this value include position and rotation
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)

#    time.sleep(4.0)

    # Go to rest position
#    motionProxy.rest()


    #Gray
    elif(key==5):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9684596061706543, 0.16213788092136383, 0.18920141458511353, 0.1429951936006546, -0.1707710176706314, 0.9848494529724121, 0.030144691467285156, -0.17985950410366058, -0.18144731223583221, -0.06150403246283531, 0.9814753532409668, -0.011181133799254894, 0.0, 0.0, 0.0, 1.0]


        fractionMaxSpeed = 1.0
        axisMask         = 63 # this value include position and rotation
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)

#    time.sleep(4.0)

    # Go to rest position
#    motionProxy.rest()
    #Brown
    elif(key==9):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9624442458152771, -0.2406195104122162, 0.1257116198539734, 0.1292807161808014, 0.2665707767009735, 0.9252750873565674, -0.26982593536376953, 0.21146260201931, -0.05139244347810745, 0.2932034730911255, 0.9546678066253662, 0.015929371118545532, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    #yellow
    elif(key==4):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9487242698669434, 0.22958898544311523, 0.21728120744228363, 0.13296592235565186, -0.24570070207118988, 0.9680595397949219, 0.04991862177848816, -0.2005704641342163, -0.1988803744316101, -0.10074515640735626, 0.974831759929657, -0.005322521552443504, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63 # this value include position and rotation
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    #    time.sleep(4.0)
    
        # Go to rest position
#    motionProxy.rest()
    #Brown
    elif(key==2):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.8432926535606384, 0.42030683159828186, 0.3349621295928955, 0.10881945490837097, -0.4554920792579651, 0.8897233009338379, 0.03032100200653076, -0.24059349298477173, -0.2852794826030731, -0.17814208567142487, 0.9417435526847839, 0.003233669325709343, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    #Green
    elif(key==1):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.8238950967788696, 0.4865782856941223, 0.2905828356742859, 0.10283416509628296, -0.5231969356536865, 0.8501009941101074, 0.059944212436676025, -0.2529323101043701, -0.2178572118282318, -0.20141978561878204, 0.9549703001976013, 0.01744747906923294, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63 # this value include position and rotation
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)

#    time.sleep(4.0)

    # Go to rest position
#    motionProxy.rest()
    #blue
    elif(key==6):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9858408570289612, -0.1288452297449112, 0.10731630027294159, 0.1444908231496811, 0.1417740285396576, 0.9822120070457458, -0.1231248527765274, 0.15719673037528992, -0.08954330533742905, 0.1365961730480194, 0.9865716695785522, -0.013898114673793316, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    #pink
    elif(key==7):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9780711531639099, -0.1738952249288559, 0.11461755633354187, 0.14017055928707123, 0.19128765165805817, 0.9677141904830933, -0.1641288697719574, 0.17636540532112122, -0.08237580955028534, 0.1824546456336975, 0.9797573089599609, -0.007139790803194046, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    #green
    elif(key==8):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9700290560722351, -0.215662881731987, 0.11195144057273865, 0.1351616531610489, 0.23392057418823242, 0.9535033702850342, -0.1900329887866974, 0.19212444126605988, -0.06576301157474518, 0.2105252742767334, 0.9753739833831787, 0.0010706502944231033, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    #red
    elif(key==10):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9423273205757141, -0.29271256923675537, 0.16229137778282166, 0.1205998957157135, 0.32878345251083374, 0.9002969264984131, -0.28524884581565857, 0.2273084670305252, -0.06261450797319412, 0.32215648889541626, 0.9446133971214294, 0.024736732244491577, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    #yellow
    elif(key==11):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9144428968429565, -0.3451070785522461, 0.2114121913909912, 0.1145780012011528, 0.3988034129142761, 0.8573272228240967, -0.32549333572387695, 0.2408529669046402, -0.06891936808824539, 0.38195696473121643, 0.9216066598892212, 0.03251896798610687, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1.0
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)    
    
def userHitNote(motionProxy, key):
    
    hit = -1
    fractionMaxSpeed = 1
    frame = motion.FRAME_TORSO
    useSensorValues = True
    diff = []
    
    if (key >= 1 and key <= 5):  
        
#        result1 = motionProxy.getTransform("RArm", frame, useSensorValues)
        

        motionProxy.post.changeAngles("RWristYaw", hit, fractionMaxSpeed)
#        motionProxy.post.angleInterpolation("RWristYaw", -1, 0.04, False)
        time.sleep(0.05)
        
        taskList = motionProxy.getTaskList()
        
#        print(taskList)
#        if len(taskList) > 0:
#            if len(taskList[0]) > 0:
#                motionProxy.killTask(taskList[0][1])
#                print("Killed")
#        motionProxy.killTask(taskList[0][1])

#        motionProxy.angleInterpolation("RWristYaw", hit, 0.05, False)
#        time.sleep(0.1)

#        time.sleep(0.05)
        '''result2 = motionProxy.getTransform("RArm", frame, useSensorValues)
        for i in range (len(result1)):
            diff.append(result2[i] - result1[i])
            
        print(key, result1, result2, diff)'''
#        motionProxy.changeAngles("RWristYaw", -hit, fractionMaxSpeed)
        motionProxy.setAngles("RWristYaw", -0.4, 1)
#        motionProxy.post.angleInterpolation("RWristYaw", 1, 0.05, False)

#        taskList = motionProxy.getTaskList()
#        
        print(taskList)
        if len(taskList) > 0:
            if len(taskList[0]) > 0:
                motionProxy.killTask(taskList[0][1])
                print("Killed")
#        motionProxy.changeAngles("RWristYaw", -hit, fractionMaxSpeed)
        
        time.sleep(0.3)
        # motionProxy.changeAngles("RWristYaw", release, 1)    

    else:
#        result1 = motionProxy.getTransform("LArm", frame, useSensorValues)
        
        motionProxy.changeAngles("LWristYaw", -hit, fractionMaxSpeed) 
#        motionProxy.post.angleInterpolation("LWristYaw", 1, 0.04, False)
        time.sleep(0.05)
#        time.sleep(0.05)
        taskList = motionProxy.getTaskList()
        
        print(taskList)
        if len(taskList) > 0:
            if len(taskList[0]) > 0:
                motionProxy.killTask(taskList[0][1])
                print("Killed")
#        motionProxy.changeAngles("LWristYaw", hit, fractionMaxSpeed)  
        '''result2 = motionProxy.getTransform("LArm", frame, useSensorValues)
        for i in range (len(result1)):
            diff.append(result2[i] - result1[i])
            
        print(key, result1, result2, diff)'''
        motionProxy.setAngles("LWristYaw", 0.4, 1)
        # motionProxy.changeAngles("LWristYaw", -release, 1)        
        time.sleep(0.3)
        
        
        


def Play(motionProxy, keys):
    for key in keys:
        if (key == 0):
            time.sleep(1)
        else:
            userSetTransform(motionProxy, key)
            time.sleep(0.5)
            userHitNote(motionProxy, key)
            
    
def main(robotIP, PORT=9559):
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)    
    
#    userInitPosture(motionProxy, postureProxy)
#    time.sleep(2)
#    userSetTransform(motionProxy)
#    time.sleep(1)

    keys = [1,1,5,5,6,6,5,0,4,4,3,3 ,2,2,1,0,
            5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
            1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
#    keys = [5,6,7,5,5,6,7,5,7,8,9,0,7,8,9,0,
#            9,10,9,8,7,5,9,10,9,8,7,5,
#            5,2,5,0,5,2,5,0]
#    keys = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

    #keys = [1,1,5,5,6,6,5,0,4,4,3,3 ,2,2,1,0,
    #        5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
    #        1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
#    keys = [5,6,7,5,5,6,7,5,7,8,9,0,7,8,9,0,
#            9,10,9,8,7,5,9,10,9,8,7,5,
#            5,2,5,0,5,2,5,0]
#    keys = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

    Play(motionProxy, keys)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
#    parser.add_argument("--ip", type=str, default="127.0.0.1",
#                        help="Robot ip address")
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
    