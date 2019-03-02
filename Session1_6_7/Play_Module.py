# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:08:33 2019

@author: CV_LAB_Howard
"""

import almath
import time
import motion
import argparse
from naoqi import ALProxy

def userInitPosture(motionProxy, postureProxy):
# =============================================================================
#     # this function should have NAO crouching position with leg joints rest/locked?
#     # and both arms should be straight down without touching legs and other parts
# =============================================================================
    postureProxy.goToPosture("Crouch", 0.5)
    time.sleep(1)
    
    chainName        = "RArm"
    frame            = motion.FRAME_TORSO

    transform       = [0.03477038815617561, 0.9961863160133362, 0.080023854970932, 0.0029639352578669786, 
                       -0.381715327501297, 0.0872393399477005, -0.9201536178588867, -0.183818519115448, 
                       -0.923625648021698,0.0014477664371952415, 0.38329294323921204, -0.10117591917514801, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    chainName        = "LArm"
    frame            = motion.FRAME_TORSO

    transform       = [0.03795033320784569, -0.9755989909172058, -0.21625538170337677, 0.006952085066586733, 
                       0.378103643655777, -0.1863023042678833, 0.9068236947059631, 0.18319708108901978, 
                       -0.9249851703643799, -0.11618120968341827, 0.36180728673934937, -0.10128530114889145, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    motionProxy.setStiffnesses("LLeg", 0.0)
    motionProxy.setStiffnesses("RLeg", 0.0)
       
# =============================================================================
# C = 1; D = 2; E = 3; F = 4; G = 5; A = 6; H = 7; C_2 = 8; D_2 = 9; E_2 = 10; F_2 = 11; 
# =============================================================================
def userSetTransform(motionProxy, key):

#    # Wake up robot
#    motionProxy.wakeUp()
#
#    # Send robot to Pose Init
#    postureProxy.goToPosture("StandInit", 0.5)

#    time.sleep(4.0)
    # Example showing how to set Torso Transform, using a fraction of max speed

    motionProxy.setStiffnesses("LArm", 0.5)
    motionProxy.setStiffnesses("RArm", 0.5)
    
    #Green C
    if(key==1):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.8013876080513, 0.4915792942047119, 0.3407750129699707, 0.11643370240926743, 
                           -0.5475539565086365, 0.8322187662124634, 0.08715841174125671, -0.2515045404434204, 
                           -0.24075406789779663, -0.2564404010772705, 0.9360959529876709, 0.01369384303689003, 
                           0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63 # this value include position and rotation

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -50*almath.TO_RAD, 1)
    # Brown D
    elif(key==2):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.8433941602706909, 0.46244972944259644, 0.2735447585582733, 0.12813331186771393, 
                           -0.4749271869659424, 0.8797256946563721, -0.0229511559009552, -0.23468232154846191, 
                           -0.25125810503959656, -0.11055696755647659, 0.9615854620933533, 0.003927379846572876, 
                           0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1
        axisMask         = 63

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -50*almath.TO_RAD, 1)
        
    #Red E
    elif (key==3):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
        
        transform = [0.9526314735412598, 0.271195650100708, 0.1376451700925827, 0.15189608931541443, 
                     -0.2941758632659912, 0.9365118741989136, 0.1908036172389984, -0.21341979503631592, 
                     -0.07716123014688492, -0.22225740551948547, 0.9719299077987671, 0.02578144520521164, 
                     0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1
        axisMask         = 63 # this value include position and rotation

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -50*almath.TO_RAD, 1)

    #yellow F
    elif(key==4):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.9594770073890686, 0.22440361976623535, 0.17043142020702362, 0.1566157341003418, 
                           -0.23924320936203003, 0.968291163444519, 0.07193642854690552, -0.19604627788066864, 
                           -0.14888443052768707, -0.10979591310024261, 0.9827401638031006, 0.00857638195157051, 
                           0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1
        axisMask         = 63 # this value include position and rotation

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -50*almath.TO_RAD, 1)
        
    #Gray G
    elif(key==5):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
        
        transform       = [0.9819556474685669, 0.12685701251029968, 0.1402507871389389, 0.16754357516765594, 
                           -0.1400074064731598, 0.9862123727798462, 0.08822131156921387, -0.1711345911026001, 
                           -0.1271255761384964, -0.10626555979251862, 0.9861777424812317, 0.004274282604455948, 
                           0.0, 0.0, 0.0, 1.0]
        
        fractionMaxSpeed = 1
        axisMask         = 63 # this value include position and rotation

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -50*almath.TO_RAD, 1)

    #blue A
    elif(key==6):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.9956784248352051, -0.09198374301195145, -0.012784874998033047, 0.17206798493862152, 
                           0.08883121609687805, 0.9834775328636169, -0.15773670375347137, 0.16309528052806854, 
                           0.02708284929394722, 0.15591934323310852, 0.9873983860015869, 0.02028868906199932, 
                           0.0, 0.0, 0.0, 1.0]
        
        fractionMaxSpeed = 1
        axisMask         = 63

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("LWristYaw", 75*almath.TO_RAD, 1)
    
    #pink B-H
    elif(key==7):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.9898942708969116, -0.137940913438797, -0.03289167582988739, 0.16925737261772156, 
                           0.12642279267311096, 0.9635026454925537, -0.23596549034118652, 0.1781325489282608, 
                           0.06424051523208618, 0.22942262887954712, 0.9712046384811401, 0.031086862087249756, 
                           0.0, 0.0, 0.0, 1.0]
        
        fractionMaxSpeed = 1
        axisMask         = 63

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("LWristYaw", 75*almath.TO_RAD, 1)
        
    #green C_2
    elif(key==8):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.9819480776786804, -0.17284922301769257, -0.07681860774755478, 0.16241022944450378, 
                           0.12994657456874847, 0.9115732908248901, -0.39006149768829346, 0.191005140542984, 
                           0.13744762539863586, 0.37303781509399414, 0.9175788164138794, 0.046224698424339294, 
                           0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1
        axisMask         = 63

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("LWristYaw", 75*almath.TO_RAD, 1)
        
    #red D_2
    elif(key==9):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.9613528847694397, -0.27436792850494385, -0.02286483347415924, 0.1525546908378601, 
                           0.2302558571100235, 0.8467550873756409, -0.4795706868171692, 0.21160534024238586, 
                           0.1509397327899933, 0.45577189326286316, 0.8772053122520447, 0.05384673550724983, 
                           0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1
        axisMask         = 63

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("LWristYaw", 75*almath.TO_RAD, 1)
        
    #yellow E_2
    elif(key==10):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.9296908378601074, -0.36800268292427063, 0.015775375068187714, 0.1415029764175415, 
                           0.3383636176586151, 0.8363217115402222, -0.4313651919364929, 0.22643716633319855, 
                           0.14555025100708008, 0.4063740670681, 0.9020394086837769, 0.05264216661453247, 
                           0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1
        axisMask         = 63

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask) 
        motionProxy.setAngles("LWristYaw", 75*almath.TO_RAD, 1)
        
    #Brown F_2
    elif(key==11):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.9143205285072327, -0.39699238538742065, 0.08009393513202667, 0.13240355253219604, 
                           0.3777778744697571, 0.7647656202316284, -0.5219361782073975, 0.2390560358762741, 
                           0.14595159888267517, 0.5074746608734131, 0.8492158651351929, 0.061654843389987946, 
                           0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63

        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("LWristYaw", 75*almath.TO_RAD, 1)
    
def userHitNote(motionProxy, key):
    
# =============================================================================
#    in case we still need it
#    hit = -0.25
#    fractionMaxSpeed = 1
#    frame = motion.FRAME_TORSO
#    useSensorValues = True
#    diff = []
# =============================================================================
    
    names      = ["RWristYaw"]
    angleLists = [[-105*almath.TO_RAD, -50*almath.TO_RAD]]
    timeLists  = [[0.05, 0.08]]
#    motionProxy.angleInterpolationBezier(names, timeLists, angleLists)
#
#    time.sleep(1.0)
    
    if (key >= 1 and key <= 5):  
                
        names      = ["RWristYaw"]
        angleLists = [[-105*almath.TO_RAD, -55*almath.TO_RAD]]
        timeLists  = [[0.05, 0.08]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

        time.sleep(0.5)

    else:  
        
        names      = ["LWristYaw"]
        angleLists = [[110*almath.TO_RAD, 75*almath.TO_RAD]]
        timeLists  = [[0.05, 0.08]]
       
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)
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
    
# =============================================================================
#    userInitPosture(motionProxy, postureProxy)
#    time.sleep(2)
#    userSetTransform(motionProxy)
#    time.sleep(1)
# =============================================================================

#    keys = [1,1,5,5,6,6,5,0,4,4,3,3 ,2,2,1,0,
#            5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
#            1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
#    keys = [5,6,7,5,5,6,7,5,7,8,9,0,7,8,9,0,
#            9,10,9,8,7,5,9,10,9,8,7,5,
#            5,2,5,0,5,2,5,0]
#    keys = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#
#    keys = [1,1,5,5,6,6,5,0,4,4,3,3 ,2,2,1,0,
#            5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
#            1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
#    keys = [5,6,7,5,5,6,7,5,7,8,9,0,7,8,9,0,
#            9,10,9,8,7,5,9,10,9,8,7,5,
#            5,2,5,0,5,2,5,0]
#    keys = [5,3,5,3,5,3,5,3,5,3,5,3,5,3,5]
    keys = [1]
#    keys = [1,2,3,4,5,6,7,8,9,10,11]


    Play(motionProxy, keys)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
# =============================================================================
#    parser.add_argument("--ip", type=str, default="127.0.0.1",
#                         help="Robot ip address")
# =============================================================================
# =============================================================================
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                         help="Robot ip address")
# =============================================================================
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
    