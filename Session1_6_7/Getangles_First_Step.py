# Use this to get all possible angles for finding different notes

import argparse
import time
import motion
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    
#    postureProxy.goToPosture("Crouch", 0.4)
    time.sleep(1)
    
    motionProxy.setStiffnesses("Head", 0.2)
    motionProxy.setStiffnesses("LLeg", 1)
    motionProxy.setStiffnesses("RLeg", 1)
#    motionProxy.setAngles("LHand", 0.22, 1)
    motionProxy.setAngles("RHand", 0.22, 1)

    
    # getting both legs angles for later set legs angles
#    names = "LHipYawPitch"
#    useSensors = True
#    sensorAngles = motionProxy.getAngles(names, useSensors)
#    print "LHipYawPitch Angles:"
#    print str(sensorAngles)
#    print ""
#    
#    names = "LHipPitch"
#    sensorAngles = motionProxy.getAngles(names, useSensors)
#    print "LHipPitch Angles:"
#    print str(sensorAngles)
#    print ""
#    
#    names = "RHipPitch"
#    sensorAngles = motionProxy.getAngles(names, useSensors)
#    print "RHipPitch Angles:"
#    print str(sensorAngles)
#    print ""
    
    # set legs angles
    names  = ["LHipYawPitch", "LHipPitch", "RHipPitch"]
    angles  = [-0.25, -0.7, -0.7]
    fractionMaxSpeed  = 0.1
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    motionProxy.setStiffnesses("LHipYawPitch", 0.2)
    motionProxy.setStiffnesses("LHipPitch", 0.2)
    motionProxy.setStiffnesses("RHipPitch", 0.2)
    motionProxy.setStiffnesses("RHipRoll", 0.0)
    motionProxy.setStiffnesses("RKneePitch", 0.0)
    motionProxy.setStiffnesses("RAnklePitch", 0.0)
    motionProxy.setStiffnesses("RAnkleRoll", 0.0)
    motionProxy.setStiffnesses("LHipRoll", 0.0)
    motionProxy.setStiffnesses("LKneePitch", 0.0)
    motionProxy.setStiffnesses("LAnklePitch", 0.0)
    motionProxy.setStiffnesses("LAnkleRoll", 0.0)
    
    tts.say("Move arm to get desired angles!")
    
    motionProxy.setStiffnesses("LArm", 0.0)
    motionProxy.setStiffnesses("RArm", 0.0)
       
    # Example that finds the difference between the command and sensed angles.

    time.sleep(10.0)
    
#    motionProxy.setStiffnesses("LArm", 1.0)
    motionProxy.setStiffnesses("RArm", 1.0)
#    motionProxy.setAngles("LHand", 0.22, 1)
    motionProxy.setAngles("RHand", 0.22, 1)

    names         = "RArm"
#    names = "LArm"
    useSensors  = True
    frame  = motion.FRAME_TORSO
#    sensorAngles = motionProxy.getAngles(names, useSensors)
#    print "Sensor angles:"
#    print str(sensorAngles)
#    print ""

    result = motionProxy.getTransform(names, frame, useSensors)
    print(result)
    tts.say("Angle recorded!")
    
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

