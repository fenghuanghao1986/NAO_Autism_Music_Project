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
        transform       = [0.8820337653160095, 0.3790297508239746, 0.2799156606197357, 
                           0.11400243639945984, -0.4082849621772766, 0.9113437533378601, 
                           0.05249696969985962, -0.24340175092220306, -0.23520147800445557, 
                           -0.16058945655822754, 0.9585881233215332, 0.025596247985959053, 
                           0.0, 0.0, 0.0, 1.0]
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
        transform       = [0.9401087760925293, 0.2323245257139206, 0.24944117665290833, 
                           0.14338093996047974, -0.24211746454238892, 0.9702064394950867, 
                           0.008875995874404907, -0.2070612907409668, -0.23994731903076172, 
                           -0.06873846799135208, 0.9683493971824646, 0.005524091422557831, 
                           0.0, 0.0, 0.0, 1.0]

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
        transform       = [0.9606088399887085, -0.21638108789920807, 0.17438435554504395, 
                           0.13190385699272156, 0.24442031979560852, 0.9564399123191833, 
                           -0.15962907671928406, 0.22714614868164062, -0.1322474479675293, 
                           0.19596418738365173, 0.9716525673866272, 0.04552464932203293, 
                           0.0, 0.0, 0.0, 1.0]
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
        transform       = [0.9099283814430237, 0.35879895091056824, 0.20807099342346191, 
                           0.1243993267416954, -0.36040198802948, 0.9322648048400879, 
                           -0.031506866216659546, -0.23131726682186127, -0.20528189837932587, 
                           -0.04632020741701126, 0.9776060581207275, 0.01880708709359169, 
                           0.0, 0.0, 0.0, 1.0]
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
        transform       = [0.7977290749549866, 0.5584625005722046, 0.22748160362243652, 
                           0.09605710208415985, -0.5727416276931763, 0.8197265267372131, 
                           -0.003929615020751953, -0.26430970430374146, -0.18866723775863647, 
                           -0.1271534115076065, 0.9737744331359863, 0.0359920971095562, 
                           0.0, 0.0, 0.0, 1.0]
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
        transform       = [0.7549957036972046, 0.6238712072372437, 0.20190632343292236, 
                           0.08934551477432251, -0.6365261673927307, 0.7712495923042297, 
                           -0.0029019415378570557, -0.2739158868789673, -0.15753060579299927, 
                           -0.12632770836353302, 0.9794004559516907, 0.04799559339880943, 
                           0.0, 0.0, 0.0, 1.0]
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
        transform       = [0.9794453382492065, -0.12720155715942383, 0.15654529631137848, 
                           0.15686027705669403, 0.1311633139848709, 0.9912441968917847, 
                           -0.015200257301330566, 0.1846284121274948, -0.1532411128282547, 
                           0.035420820116996765, 0.9875536561012268, 0.008092634379863739, 
                           0.0, 0.0, 0.0, 1.0]
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
        transform       = [0.9669263362884521, -0.18347570300102234, 0.17717286944389343, 
                           0.14802011847496033, 0.1927211582660675, 0.9805812835693359, 
                           -0.03631642460823059, 0.20442283153533936, -0.167069211602211, 
                           0.06926026940345764, 0.9835095405578613, 0.01827755756676197, 
                           0.0, 0.0, 0.0, 1.0]
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
        transform       = [0.97382652759552, -0.18728788197040558, 0.12878389656543732, 
                           0.1423220932483673, 0.20739543437957764, 0.9640157222747803, 
                           -0.16631534695625305, 0.21658730506896973, -0.0930008515715599, 
                           0.18867149949073792, 0.9776267409324646, 0.03856509178876877, 
                           0.0, 0.0, 0.0, 1.0]
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
        transform       = [0.9093157052993774, -0.3619553744792938, 0.20526385307312012, 
                           0.11645516753196716, 0.4004344940185547, 0.895296573638916, 
                           -0.19518250226974487, 0.2490326315164566, -0.11312466859817505, 
                           0.2596772313117981, 0.9590466618537903, 0.05591168254613876, 
                           0.0, 0.0, 0.0, 1.0]
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
        transform       = [0.8770732879638672, -0.42776089906692505, 0.2185472548007965, 
                           0.10589532554149628, 0.4709978699684143, 0.8551942110061646, 
                           -0.21634218096733093, 0.25902336835861206, -0.09435762465000153, 
                           0.2926832437515259, 0.9515424966812134, 0.06389060616493225, 
                           0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1.0
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)    
    
def userHitNote(motionProxy, key):
    
    hit = -1
    fractionMaxSpeed = 1
    
    if (key >= 1 and key <= 5):   
        motionProxy.changeAngles("RWristYaw", hit, fractionMaxSpeed)
        time.sleep(0.04)
#        time.sleep(0.05)
#        motionProxy.changeAngles("RWristYaw", -hit, fractionMaxSpeed)
        motionProxy.setAngles("RWristYaw", -0.4, 1)
        
        time.sleep(0.5)
        # motionProxy.changeAngles("RWristYaw", release, 1)        
    else:
        motionProxy.changeAngles("LWristYaw", -hit, fractionMaxSpeed)        
        time.sleep(0.04)
#        time.sleep(0.05)
#        motionProxy.changeAngles("LWristYaw", hit, fractionMaxSpeed)    
        motionProxy.setAngles("LWristYaw", 0.4, 1)
        # motionProxy.changeAngles("LWristYaw", -release, 1)        
        time.sleep(0.5)

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
    
    userInitPosture(motionProxy, postureProxy)
    time.sleep(2)
#    userSetTransform(motionProxy)
#    time.sleep(1)
    #keys = [1,1,5,5,6,6,5,0,4,4,3,3 ,2,2,1,0,
    #        5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
    #        1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
#    keys = [5,6,7,5,5,6,7,5,7,8,9,0,7,8,9,0,
#            9,10,9,8,7,5,9,10,9,8,7,5,
#            5,2,5,0,5,2,5,0]
    keys = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
    Play(motionProxy, keys)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
#    parser.add_argument("--ip", type=str, default="192.168.0.2",
#                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
    