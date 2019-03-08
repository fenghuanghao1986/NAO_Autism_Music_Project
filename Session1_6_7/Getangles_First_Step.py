# Use this to get all possible angles for finding different notes

import argparse
import time
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    
    postureProxy.goToPosture("Crouch", 0.4)
    time.sleep(1)
    
    motionProxy.setStiffnesses("Head", 0.0)
    motionProxy.setStiffnesses("LLeg", 0.2)
    motionProxy.setStiffnesses("RLeg", 0.2)
    
    # getting both legs angles for later set legs angles
    names = "LHipYawPitch"
    useSensors = True
    sensorAngles = motionProxy.getAngles(names, useSensors)
    print "LHipYawPitch Angles:"
    print str(sensorAngles)
    print ""
    
    names = "LHipPitch"
    sensorAngles = motionProxy.getAngles(names, useSensors)
    print "LHipPitch Angles:"
    print str(sensorAngles)
    print ""
    
    names = "RHipPitch"
    sensorAngles = motionProxy.getAngles(names, useSensors)
    print "RHipPitch Angles:"
    print str(sensorAngles)
    print ""
    
    # Example that finds the difference between the command and sensed angles.
#    names         = "RArm"
    names = "LArm"
    useSensors  = True
    sensorAngles = motionProxy.getAngles(names, useSensors)
    print "Sensor angles:"
    print str(sensorAngles)
    print ""
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
#    parser.add_argument("--ip", type=str, default="192.168.0.2",
#                        help="Robot ip address")
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)

