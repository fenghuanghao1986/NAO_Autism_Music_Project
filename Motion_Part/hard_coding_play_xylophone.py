# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 14:40:45 2018

@author: fengh
"""

# this code is to test the very first time NAO play xylophone motion

# import packages
import almath
import argparse
import motion
import random
import sys
import time
from naoqi import ALProxy

maxSpeed = 1.0

def initRobotPosition(motionProxy, postureProxy):
    ''' Inits NAO's position and stiffnesses'''

    # motionProxy.wakeUp()
    # postureProxy.goToPosture("Crouch", 1.0)
    
    time.sleep(1.0)
    # Make both arms stiff.

    motionProxy.setStiffnesses("LArm", 1.0)
    motionProxy.setStiffnesses("RArm", 1.0)
    # Make head in the right position and keep stiff.
    motionProxy.setAngles("HeadPitch", 0.4, 1.0)
    # Make arm to initial position and ready for everything.
    motionProxy.setAngles("RShoulderPitch", 0.75, 1.0)
    motionProxy.setAngles("LShoulderPitch", 0.75, 1.0)
    
    time.sleep(1.0)
    
    motionProxy.setAngles("RShoulderRoll", -1.2, 1.0)
    motionProxy.setAngles("LShoulderRoll", 1.2, 1.0)
    
    time.sleep(1.0)
    
    motionProxy.setAngles("RWristYaw", -0.4, 1.0)
    motionProxy.setAngles("LWristYaw", 0.4, 1.0)
         
    time.sleep(1.0)
'''    
def handControl(motionProxy, postureProxy, touchProxy):
    
    LLHand = touchProxy.HandLeftLeftTouched()
    LRHand = touchProxy.HandLeftRightTouched()
    RLHand = touchProxy.HandRightLeftTouched()
    RRHand = touchProxy.HandRightRightTouched()
        
    while(1):
        
        if(RLHand and RRHand):        
            motionProxy.openHand('RHand')
            
        else:
            motionProxy.closeHand('RHand')
        
        if (LLHand and LRHand):       
            motionProxy.openHand('LHand')
            
        else:
            motionProxy.closeHand('LHand')
    
'''    
def hitBarWrist(motionProxy, postureProxy):
    
    hit = -1
    fractionMaxSpeed = 1
          
    motionProxy.changeAngles("RWristYaw", hit, fractionMaxSpeed)
    time.sleep(0.04)
        
    motionProxy.setAngles("RWristYaw", -0.4, 1.0)
        
    time.sleep(0.5)
    # motionProxy.changeAngles("RWristYaw", release, 1)        
        
    motionProxy.changeAngles("LWristYaw", -hit, fractionMaxSpeed)        
    time.sleep(0.04)
        
    motionProxy.setAngles("LWristYaw", 0.4, 1.0)
    # motionProxy.changeAngles("LWristYaw", -release, 1)        
    time.sleep(0.5)
    '''
    names  = "Head"
    # We still need to specify the correct number of target angles
    targetAngles     = [0.5, 0.25]
    maxSpeedFraction = 1 # Using 20% of maximum joint speed
    motionProxy.angleInterpolationWithSpeed(names, targetAngles, maxSpeedFraction)
    '''
    
def moveShoulder(motionProxy, postureProxy):
    
    # change = [-0.08, -0.04, 0.04, 0.08]
    change = [0, 0]
    
    motionProxy.changeAngles("RShoulderRoll", random.choice(change), 1.0)
    motionProxy.changeAngles("LShoulderRoll", -random.choice(change), 1.0)
    
  
def userArmsCartesian(motionProxy):
    effector   = ["LArm", "RArm"]
    frame      = motion.FRAME_TORSO
    useSensorValues = False

    # just control position
    axisMask   = [motion.AXIS_MASK_VEL, motion.AXIS_MASK_VEL]

    # LArm path
    pathLArm = []
    initTf   = almath.Transform(motionProxy.getTransform("LArm", frame, useSensorValues))
    targetTf = almath.Transform(motionProxy.getTransform("LArm", frame, useSensorValues))
    targetTf.r1_c4 += 0.04 # x
    targetTf.r2_c4 -= 0.10 # y
    targetTf.r3_c4 += 0.10 # z
    pathLArm.append(list(targetTf.toVector()))
    pathLArm.append(list(initTf.toVector()))
    pathLArm.append(list(targetTf.toVector()))
    pathLArm.append(list(initTf.toVector()))

    # RArm path
    pathRArm = []
    initTf   = almath.Transform(motionProxy.getTransform("RArm", frame, useSensorValues))
    targetTf = almath.Transform(motionProxy.getTransform("RArm", frame, useSensorValues))
    targetTf.r1_c4 += 0.04 # x
    targetTf.r2_c4 += 0.10 # y
    targetTf.r3_c4 += 0.10 # z
    pathRArm.append(list(targetTf.toVector()))
    pathRArm.append(list(initTf.toVector()))
    pathRArm.append(list(targetTf.toVector()))
    pathRArm.append(list(initTf.toVector()))

    pathList = []
    pathList.append(pathLArm)
    pathList.append(pathRArm)

    # Go to the target and back again
    timesList = [[1.0, 2.0, 3.0, 4.0],
                 [1.0, 2.0, 3.0, 4.0]] # seconds

    motionProxy.transformInterpolations(effector, frame, pathList,
                                       axisMask, timesList)    
def main(robotIP, PORT=9559):
    
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    # touchProxy   = ALProxy("ALTouch", robotIP, PORT)
        
    initRobotPosition(motionProxy, postureProxy)    
    # handControl(motionProxy, postureProxy, touchProxy)
    
    for i in range(0, 4):
                       
        moveShoulder(motionProxy, postureProxy)
        time.sleep(0.25)
        
        hitBarWrist(motionProxy, postureProxy)
        #time.sleep(1)
        
    
    
    
    '''
    # effector   = "LArm"
    frame      = motion.FRAME_TORSO
    axisMask   = almath.AXIS_MASK_VEL # just control position
    useSensorValues = False

    path = []
    currentTf = motionProxy.getTransform(armName, frame, useSensorValues)
    targetTf  = almath.Transform(currentTf)
    targetTf.r1_c4 -= 0 # x
    targetTf.r2_c4 += 0.1 # y
    targetTf.r3_c4 += 0 # z
    
    path.append(list(targetTf.toVector()))
    path.append(currentTf)

    # Go to the target and back again
    times      = [2.0, 4.0] # seconds

    motionProxy.transformInterpolations(armName, frame, path, axisMask, times)

    
    '''
    # Go to rest position
    # motionProxy.rest()
'''
def interpretJointsPose(motionProxy, memoryProxy):

    # Retrieve current arm position.
    armPose = motionProxy.getAngles(armName, True)

    targetX     = 0.0
    targetY     = 0.0
    targetTheta = 0.0
    gaitConfig = motionProxy.getMoveConfig("Default")

    # Filter Shoulder Pitch.
    if (armPose[0] > - 0.9 and armPose[0] < -0.20):
        targetX = stepLength
    elif (armPose[0] > -2.5 and armPose[0] < -1.5):
        targetX = - stepLength - 0.02

    # Filter Wrist Yaw.
    if armPose[4] > 0.2:
        targetTheta = gaitConfig[2][1]
    elif armPose[4] < -0.2:
        targetTheta = - gaitConfig[2][1]

    # Return corresponding pose.
    return almath.Pose2D(targetX, targetY, targetTheta)
'''



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    '''
    parser.add_argument("--ip", type=str, default="169.254.254.250",
                        help="Robot ip address")
    '''
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)