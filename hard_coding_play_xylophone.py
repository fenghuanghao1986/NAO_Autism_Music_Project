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
import sys
import time
from naoqi import ALProxy

maxSpeed = 1.0

def initRobotPosition(motionProxy, postureProxy):
    ''' Inits NAO's position and stiffnesses'''

    motionProxy.wakeUp()
    postureProxy.goToPosture("Crouch", 1.0)
    
    time.sleep(1.0)
    # Make both arms stiff.

    motionProxy.setStiffnesses("LArm", 1.0)
    motionProxy.setStiffnesses("RArm", 1.0)
    # Make head in the right position and keep stiff.
    motionProxy.setAngles("HeadPitch", 0.4, 1.0)
    # Make arm to initial position and ready for everything.
    motionProxy.setAngles("RShoulderPitch", 0.5, 1.0)
    motionProxy.setAngles("LShoulderPitch", 0.5, 1.0)
    
    time.sleep(1.0)
    
    motionProxy.setAngles("RShoulderRoll", -0.8, 1.0)
    motionProxy.setAngles("LShoulderRoll", 0.8, 1.0)
    
    time.sleep(1.0)
    
    motionProxy.setAngles("RWristYaw", -0.6, 1.0)
    motionProxy.setAngles("LWristYaw", 0.6, 1.0)
         
    time.sleep(1.0)
    
def hitBarWrist(motionProxy, postureProxy):
    
    hit = -0.6
    fractionMaxSpeed = 1
          
    motionProxy.changeAngles("RWristYaw", hit, fractionMaxSpeed)
    time.sleep(0.1)
        
    motionProxy.setAngles("RWristYaw", -0.6, 1.0)
        
    time.sleep(0.8)
    # motionProxy.changeAngles("RWristYaw", release, 1)        
        
    motionProxy.changeAngles("LWristYaw", -hit, fractionMaxSpeed)        
    time.sleep(0.1)
        
    motionProxy.setAngles("LWristYaw", 0.6, 1.0)
    # motionProxy.changeAngles("LWristYaw", -release, 1)        
    time.sleep(0.8)
    
def moveShoulder(motionProxy, postureProxy):
    
    motionProxy.changeAngles("RShoulderRoll", -0.08, 1.0)
    motionProxy.changeAngles("LShoulderRoll", 0.08, 1.0)
    
    
def main(robotIP, PORT=9559):
    
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    # motionProxy.wakeUp()

    # Send robot to Stand Init
    #postureProxy.goToPosture("StandInit", 0.5)
    initRobotPosition(motionProxy, postureProxy)
    hitBarWrist(motionProxy, postureProxy)
    moveShoulder(motionProxy, postureProxy)
    
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
    motionProxy.rest()
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
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)