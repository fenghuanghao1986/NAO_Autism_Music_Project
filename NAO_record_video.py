# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 18:03:05 2018

@author: fengh
"""

import sys
import time
from naoqi import ALProxy

if __name__ == "__main__":
    IP = "127.0.0.1"  # Replace here with your NaoQi's IP address.
    PORT = 9559

     # Read IP address from first argument if any.
    if len(sys.argv) > 1:
        IP = sys.argv[1]

    videoRecorderProxy = ALProxy("ALVideoRecorder", IP, PORT)

    # This records a 320*240 MJPG video at 10 fps.
    # Note MJPG can't be recorded with a framerate lower than 3 fps.
    videoRecorderProxy.setResolution(1)
    videoRecorderProxy.setFrameRate(10)
    videoRecorderProxy.setVideoFormat("MJPG")
    videoRecorderProxy.startRecording("/home/nao/recordings/cameras", "myvideo")

    time.sleep(5)

    # Video file is saved on the robot in the
    # /home/nao/recordings/cameras/ folder.
    videoInfo = videoRecorderProxy.stopRecording()

    print "Video was saved on the robot: ", videoInfo[1]
    print "Num frames: ", videoInfo[0]
    
    