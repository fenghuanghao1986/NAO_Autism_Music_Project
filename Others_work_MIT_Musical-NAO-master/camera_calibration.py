import sys
from naoqi import ALProxy
import time
import almath
from random import randint
import motion
from matplotlib import pyplot as plt
import cv2
from PIL import Image
import glob
import numpy as np

##########################################################
####################### Functions ########################
##########################################################

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def initial_pos():
    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("Stand", 0.5)
    motionProxy.setStiffnesses("Head", 1.0)
    motionProxy.setStiffnesses("LHand", 1.0)
    motionProxy.setStiffnesses("LArm", 1.0)
    time.sleep(2.0)     # wait for 2 second before move to next action

def get_image(IP, PORT):
    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    camera = 1  # 1 = bottom camera
    resolution = 2  # 2 = VGA
    colorSpace = 11  # RGB

    videoClient = camProxy.subscribeCamera("python_client", camera, resolution, colorSpace, 5)

    t0 = time.time()

    # Get a camera image.
    # image[6] contains the image data passed as an array of ASCII chars.
    naoImage = camProxy.getImageRemote(videoClient)

    t1 = time.time()

    # Time the image transfer.
    print "acquisition delay ", t1 - t0

    camProxy.unsubscribe(videoClient)

    # Now we work with the image returned and save it as a PNG  using ImageDraw
    # package.

    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]

    return array, imageWidth, imageHeight



##########################################################
###################### "MAIN"  ###########################
##########################################################

with open('config.txt') as data_file:     #Read Robot IP and Port from the config.txt file
    data = json.loads(data_file.read())

robotIP = str(data["robotIP"])
PORT = int(data["PORT"])

tts = ALProxy("ALTextToSpeech", robotIP, PORT)
motionProxy = ALProxy("ALMotion", robotIP, PORT)
postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

initial_pos()     # Function initial_pos put the arms into the initial state above the metallophone

for i in range(0, 30):
    array, imageWidth, imageHeight = get_image(robotIP, PORT)

    #Create a PIL Image from our pixel array.
    im = Image.frombytes("RGB", (imageWidth, imageHeight), array)

    # Save the image.
    im.save('calibration/' + str(i) + '.png', "PNG")   # Save images into calibration folder

############################################################################

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((7*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:7].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('calibration/*.png')  # Read images with checkerboards

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (9,7),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)


        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (9,7), corners2,ret)

        im = Image.frombytes("RGB", (imageWidth, imageHeight), img)

        cv2.imshow('img',img)
        # im.save(str(fname) + str(2)+ '.png', "PNG")
        cv2.waitKey(500)

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

print "dist", dist

print "camera matrix:", mtx



