

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    motionProxy = ALProxy("ALMotion", robotIP, PORT)

    # Example that finds the difference between the command and sensed angles.
    names         = "Body"
    useSensors    = False
    commandAngles = motionProxy.getAngles(names, useSensors)
    print "Command angles:"
    print str(commandAngles)
    print ""

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
#    parser.add_argument("--ip", type=str, default="192.168.0.2",
#                        help="Robot ip address")
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)






































