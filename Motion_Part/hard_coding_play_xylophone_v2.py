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

    motionProxy.setStiffnesses("LArm", 1)
    motionProxy.setStiffnesses("RArm", 1)
    
    motionProxy.setStiffnesses("LLeg", 0.0)
    motionProxy.setStiffnesses("RLeg", 0.0)
    
    #Green
    if(key==1):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.7417324185371399, 0.5906713604927063, 0.3177109956741333, 0.1021602600812912, -0.6202605962753296, 0.7843306064605713, -0.010116875171661377, -0.255073606967926, -0.2551662027835846, -0.18955959379673004, 0.9481335878372192, 0.00217537023127079, 0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63 # this value include position and rotation
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -0.8, 1)
        time.sleep(.5)
        names      = ["RWristYaw"]
        angleLists = [[-1.91, -1.0431618690490723]]
        timeLists  = [[0.04, 0.07]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)
    # Brown
    elif(key==2):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.8780239224433899, 0.4393429756164551, 0.18987341225147247, 0.12202411144971848, -0.4633156657218933, 0.8797175884246826, 0.10693711042404175, -0.23434928059577942, -0.12005291879177094, -0.1818646788597107, 0.975967526435852, 0.012157795950770378, 0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -0.8, 1)
        time.sleep(.5)
        names      = ["RWristYaw"]
        angleLists = [[-1.96, -1.0937838554382324]]
        timeLists  = [[0.03, 0.07]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)
    
    #Red
    elif (key==3):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
#        transform       = [0.938517153263092, 0.26535412669181824, 0.2208453118801117, 0.1289231777191162, -0.29033753275871277, 0.9527726173400879, 0.08904257416725159, -0.21311216056346893, -0.18678754568099976, -0.14768767356872559, 0.9712357521057129, 0.003036290407180786, 0.0, 0.0, 0.0, 1.0]
        transform = [0.9212828874588013, 0.3758701682090759, 0.099796824157238, 0.13551205396652222, -0.38620278239250183, 0.9144043922424316, 0.12129291892051697, -0.211635023355484, -0.045664262026548386, -0.15028689801692963, 0.9875872135162354, 0.0080105010420084, 0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63 # this value include position and rotation
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -1, 1)
        time.sleep(.5)
        names      = ["RWristYaw"]
        angleLists = [[-2.15, -1.279397964477539]]
        timeLists  = [[0.04, 0.07]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)

    #yellow
    elif(key==4):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9264622926712036, 0.36433541774749756, 0.09448415786027908, 0.13288673758506775, -0.36880332231521606, 0.9288653135299683, 0.0345437228679657, -0.19243009388446808, -0.07517755031585693, -0.06684952974319458, 0.9949268102645874, -0.008625689893960953, 0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63 # this value include position and rotation
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -1, 1)
        time.sleep(.5)
        names      = ["RWristYaw"]
        angleLists = [[-2.24, -1.3745059967041016]]
        timeLists  = [[0.05, 0.08]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)
        
    #Gray
    elif(key==5):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
        
        transform       = [0.959071159362793, 0.2789939343929291, 0.04842231050133705, 0.14187568426132202, -0.2808551788330078, 0.9590335488319397, 0.03707994520664215, -0.17000512778759003, -0.036093540489673615, -0.049161963164806366, 0.9981383085250854, -0.008929341100156307, 0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63 # this value include position and rotation
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -1.1, 1)
        time.sleep(.5)
        names      = ["RWristYaw"]
        angleLists = [[-2.34, -1.469614028930664]]
        timeLists  = [[0.05, 0.08]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)


    #blue
    elif(key==6):
        chainName        = "RArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9676035046577454, 0.2508425712585449, 0.028659865260124207, 0.1457143872976303, -0.2515961229801178, 0.9674654006958008, 0.02665035054087639, -0.14819003641605377, -0.021042386069893837, -0.03299768269062042, 0.9992339015007019, -0.01215360313653946, 0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("RWristYaw", -1.3, 1)
        time.sleep(.5)
        names      = ["RWristYaw"]
        angleLists = [[-2.5, -1.6352858543395996]]
        timeLists  = [[0.05, 0.1]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)
    
    #pink
    elif(key==7):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.969535768032074, -0.2427014708518982, -0.03311120346188545, 0.14519064128398895, 0.22328346967697144, 0.9312502145767212, -0.2879539132118225, 0.18470138311386108, 0.10072165727615356, 0.27178844809532166, 0.9570716023445129, 0.017699655145406723, 0.0, 0.0, 0.0, 1.0]
        
        fractionMaxSpeed = 1
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("LWristYaw", 1.4864040613174438, 1)
        time.sleep(.5)
        names      = ["LWristYaw"]
        angleLists = [[2.2, 1.4864040613174438]]
        timeLists  = [[0.05, 0.08]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)
        
    #green
    elif(key==8):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9245267510414124, -0.3730473518371582, 0.07801258563995361, 0.12383995950222015, 0.3810974657535553, 0.9028229117393494, -0.19918692111968994, 0.20624247193336487, 0.0038745999336242676, 0.21388402581214905, 0.9768513441085815, 0.004980376921594143, 0.0, 0.0, 0.0, 1.0]

        fractionMaxSpeed = 1
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("LWristYaw", 1.3943641185760498, 1)
        
        time.sleep(.5)
        names      = ["LWristYaw"]
        angleLists = [[2.30, 1.3943641185760498]]
        timeLists  = [[0.05, 0.08]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
        
        
    #red
    elif(key==9):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.8985764980316162, -0.42378586530685425, 0.11386728286743164, 0.11630624532699585, 0.43803277611732483, 0.8507416248321533, -0.2904582619667053, 0.2268935590982437, 0.026220470666885376, 0.3108765780925751, 0.9500885605812073, 0.018442030996084213, 0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("LWristYaw", 1.348344087600708, 1)
        time.sleep(.5)
        names      = ["LWristYaw"]
        angleLists = [[2.24, 1.348344087600708]]
        timeLists  = [[0.05, 0.08]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)
        
    #yellow
    elif(key==10):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO
    #    transform        = [1.0, 0.0, 0.0, 0.00,
    #                        0.0, 1.0, 0.0, 0.00,
    #                        0.0, 0.0, 1.0, 0.25]
        transform       = [0.9170975089073181, -0.39322495460510254, 0.06562250107526779, 0.12005940079689026, 0.37656670808792114, 0.8004097938537598, -0.4664135277271271, 0.23387812077999115, 0.13088054955005646, 0.4524579346179962, 0.8821293115615845, 0.04614535719156265, 0.0, 0.0, 0.0, 1.0]
        
        fractionMaxSpeed = 1
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask) 
        motionProxy.setAngles("LWristYaw", 1.333004117012024, 1)
        time.sleep(.5)
        names      = ["LWristYaw"]
        angleLists = [[2, 1.2256240844726562]]
        timeLists  = [[0.05, 0.08]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)
        
#Brown
    elif(key==11):
        chainName        = "LArm"
        frame            = motion.FRAME_TORSO

        transform       = [0.7812172770500183, -0.5827138423919678, 0.22392860054969788, 0.09143239259719849, 0.6209056377410889, 0.7624403238296509, -0.18210135400295258, 0.255689412355423, -0.06461922079324722, 0.28129926323890686, 0.9574418067932129, 0.017450857907533646, 0.0, 0.0, 0.0, 1.0]
        fractionMaxSpeed = 1
        axisMask         = 63
    #    axisMask   = motion.AXIS_MASK_VEL
    #    print(motion.AXIS_MASK_VEL)
        motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        motionProxy.setAngles("LWristYaw", 1.201080083847046, 1)
        time.sleep(.5)
        names      = ["LWristYaw"]
        angleLists = [[2.07, 1.201080083847046]]
        timeLists  = [[0.05, 0.08]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

#        time.sleep(0.3)
#        time.sleep(.5)
    
def userHitNote(motionProxy, key):
    
#    hit = -0.25
#    fractionMaxSpeed = 1
#    frame = motion.FRAME_TORSO
#    useSensorValues = True
#    diff = []
    
#    motionProxy.angleInterpolationBezier(names, timeLists, angleLists)
#
#    time.sleep(1.0)
    
    if (key >= 1 and key <= 5):  
                
        names      = ["RWristYaw"]
        angleLists = [[-105*almath.TO_RAD, -55*almath.TO_RAD]]
        timeLists  = [[0.05, 0.08]]
        
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)

        time.sleep(0.3)

    else:  
        
        names      = ["LWristYaw"]
        angleLists = [[110*almath.TO_RAD, 95*almath.TO_RAD]]
        timeLists  = [[0.05, 0.08]]
       
        motionProxy.angleInterpolationBezier(names, timeLists, angleLists)
        time.sleep(0.3)


def Play(motionProxy, keys):
    for key in keys:
        if (key == 0):
            time.sleep(1)
        else:
            userSetTransform(motionProxy, key)
            time.sleep(0.1)
#            userHitNote(motionProxy, key)
            
    
def main(robotIP, PORT=9559):
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)    
    
#    userInitPosture(motionProxy, postureProxy)
#    time.sleep(2)
#    userSetTransform(motionProxy)
#    time.sleep(1)

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
    keys = [1,2,3,4,5,6,7,8,9,10,11]
#    keys = [7,10,7,10,7,10]


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
    