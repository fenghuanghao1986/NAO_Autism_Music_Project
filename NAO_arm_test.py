# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:10:58 2018

@author: fengh
"""

import argparse
import motion
import almath
import time

from naoqi import ALProxy

armName     = "LArm"
lFootOffset = almath.Pose2D(0.0, 0.09, 0.0)
rFootOffset = almath.Pose2D(0.0, -0.09, 0.0)
stepSpeed   = 1.0
stepLength  = 0.05

def initRobotPosition(motionProxy, postureProxy):
    ''' Inits NAO's position and stiffnesses to make the guiding possible.'''
    
    global armName
    
    motionProxy.wakeUp()
    postureProxy.goToPosture("StandInit", 0.3)
    motionProxy.moveInit()
    time.sleep(1.0)
    # Make left arm loose.
    motionProxy.setAngles("LWristYaw", 0.0, 1.0)
    motionProxy.setAngles("Head", [0.44, -0.44], 0.5)
    motionProxy.setStiffnesses(armName, 0.0)
    motionProxy.setStiffnesses("LWristYaw", 0.2)

    # Disable arm moves while walking on left arm.
    motionProxy.setMoveArmsEnabled(False, True)
    time.sleep(1.0)
    
def interpretJointsPose(motionProxy, memoryProxy):
    ''' Translates the current left arm pose into a target position for NAO's
        foot. '''

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
    
def main(robotIP, PORT=9559):

    global armName
    
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # effector   = "LArm"
    frame      = motion.FRAME_TORSO
    axisMask   = almath.AXIS_MASK_VEL # just control position
    useSensorValues = False

    path = []
    currentTf = motionProxy.getTransform(armName, frame, useSensorValues)
    targetTf  = almath.Transform(currentTf)
    targetTf.r1_c4 -= 0 # x
    targetTf.r2_c4 += 0 # y
    targetTf.r3_c4 += 0.3
    
    path.append(list(targetTf.toVector()))
    path.append(currentTf)

    # Go to the target and back again
    times      = [2.0, 4.0] # seconds

    motionProxy.transformInterpolations(armName, frame, path, axisMask, times)

    # Go to rest position
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)


