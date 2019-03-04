

import argparse
from naoqi import ALProxy
import time

def main(robotIP, PORT=9559):
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    
    motionProxy.rest()
    motionProxy.setStiffnesses("LArm", 0)
    motionProxy.setStiffnesses("RArm", 0)
    
    time.sleep(5)
    motionProxy.setStiffnesses("RArm", 1)

    # Example that finds the difference between the command and sensed angles.
    names         = "RArm"
    useSensors    = False
    commandAngles = [0.6550600528717041, -0.3145120143890381, 1.405102014541626, 0.6811380386352539, -0.7470998764038086, 0.23559999465942383]
    print "Command angles:"
    print str(commandAngles)
    print ""

    angles  = commandAngles
    fractionMaxSpeed  = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    time.sleep(5.0)
    
    useSensors  = True
    sensorAngles = motionProxy.getAngles(names, useSensors)
    print "Sensor angles:"
    print str(sensorAngles)
    print ""
    
    difference = list(set(commandAngles) - set(sensorAngles))
    print(difference)
    errors = []
    for i in range(0, len(commandAngles)):
        errors.append(commandAngles[i]-sensorAngles[i])
    print "Errors"
    print errors


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






































