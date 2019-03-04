# This code is part of the master project Musical NAO. Python interpreter used: 2.7.10
# This code tested on V5 and V6 robots

"""  
                   |\                         __3__          |         
____|\_______________|\\_______________|_______'__|__`___|_____|___|__________
____|/___3_|________@'_\|__|_____|_____|___|___|__|__|___|_|__@'___|___|___|__
___/|____-_|____________|__|_____|____@'___|__@'_@'_@'___|_|______@'___|___|__
__|_/_\__4_|___|_______@'__|____O'_________|____________O'_|__________@'___|__
___\|/_____|___|___________|_______________|_______________|_______________|__
    /         O'           Musical NAO | Author: Ioannis Papakonstantinopoulos

"""

# Short description:
# The goal of this project is to make NAO locate the metallophone in the 3D space and adjust its arms position in order
# to hit successfully the metallophone.
#
# Vision Part:
# For the 3D pose estimation we use the bottom camera of the robot for capturing
# images in our computer. We also use the OpenCV library and the solvePnP algorithm for estimating the 3D position of
# the object. The solvePnP takes as arguments some points (in our case 5) in the 3D object and the corresponding 2D
# points of the captured image, and returns the rotation and translation of the object with respect to the camera.
# We track the 2D points using a model image with known x,y positions of the points. We use the SIFT algorithm to
# extract key points of the current image and the model image and using the BruteForceMatcher algorithm we find the
# homography matrix between the two images. With this we can track the particular 2D points that we want.

# Kinematics Part:
# We use the Robotics Toolbox in matlab in order to pre-calculate the inverse kinematics of the NAO's arms holding the
# sticks. We save the results in csv files and we import them in python. The csv files contain the x and y coordinates
# with respect to the Torso frame of the robot and their corresponding angles for each motor (Forward Kinematics).

# Visual-Servoing:
# In this part the robot places the end-effectors above the Mi notes (left and right), then using again the bottom
# camera we capture an image which contains the end-effectors. Ten using the cv2.projectPoints() function we project
# the 2D position of the desired position of the beaters and using the Hough circle detection algorithm, we detect the
# actual position of the beaters. Then in a while loop we correct the error in the z and y axes setting a threshold.
#



import sys
import time
import almath
from random import randint
import motion
from matplotlib import pyplot as plt
import cv2
import numpy as np
import math
from capture_image import capture_image
from pose import pose
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import json
import glob
from PIL import Image

##########################################################
#################### ~ Functions ~ #######################
##########################################################


def stiffness_on(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def initial_pos():
    # First stage of the initial position in order to avoid collision with the table
    # Initialize position of left Arm
    LSR = 44 * almath.TO_RAD
    LSP = 75 * almath.TO_RAD
    LER = -44 * almath.TO_RAD
    LEY = -100 * almath.TO_RAD
    LWY = -47 * almath.TO_RAD
    LH = 10 * almath.TO_RAD

    names = ["LShoulderRoll", "LShoulderPitch", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]
    angles = [LSR, LSP, LEY, LER, LWY, LH]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    # Initialize position of right Arm
    RSR = -44 * almath.TO_RAD
    RSP = 75 * almath.TO_RAD
    RER = 44 * almath.TO_RAD
    REY = 100 * almath.TO_RAD
    RWY = 47 * almath.TO_RAD
    RH = 10 * almath.TO_RAD

    names = ["RShoulderRoll", "RShoulderPitch", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angles = [RSR, RSP, REY, RER, RWY, RH]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(0.5)

    # Second stage of the initial position
    LSR = 40 * almath.TO_RAD
    LSP = -1 * almath.TO_RAD
    LER = 0 * almath.TO_RAD
    LEY = 0 * almath.TO_RAD
    LWY = -14 * almath.TO_RAD
    LH = 10 * almath.TO_RAD

    names = ["LShoulderRoll", "LShoulderPitch", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]
    angles = [LSR, LSP, LEY, LER, LWY, LH]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    RSR = -40 * almath.TO_RAD
    RSP = -1 * almath.TO_RAD
    RER = 0 * almath.TO_RAD
    REY = 0 * almath.TO_RAD
    RWY = 14 * almath.TO_RAD
    RH = 10 * almath.TO_RAD

    names = ["RShoulderRoll", "RShoulderPitch", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angles = [RSR, RSP, REY, RER, RWY, RH]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    time.sleep(2.0)     # wait for 2 second before move to next action


def l_hit(temp):
    names = "LWristYaw"

    if temp == 0:
        #              2 angles
        anglePath = [10.0 * almath.TO_RAD, 0.0 * almath.TO_RAD]
        timeLists = [0.068, 0.076]
    elif temp == 1:
        anglePath = [12.0*almath.TO_RAD, 0.0 * almath.TO_RAD]
        timeLists  = [0.071, 0.081]
    elif temp == 2:
        anglePath = [14.0 * almath.TO_RAD, 0.0 * almath.TO_RAD]
        timeLists = [0.080, 0.09]
    elif temp == 3:
        anglePath = [16.0 * almath.TO_RAD, 0.0 * almath.TO_RAD]
        timeLists = [0.093, 0.107]

    isAbsolute = True
    motionProxy.angleInterpolation(names, anglePath, timeLists, isAbsolute)
    time.sleep(0.2)


def r_hit(temp):
    names = "RWristYaw"

    if temp == 0:
        anglePath = [-10.0 * almath.TO_RAD, 0.0 * almath.TO_RAD]
        timeLists = [0.068, 0.076]
    elif temp == 1:
        anglePath = [-12.0*almath.TO_RAD, 0.0*almath.TO_RAD]
        timeLists  = [0.071, 0.081]
    elif temp == 2:
        anglePath = [-14.0 * almath.TO_RAD, 0.0 * almath.TO_RAD]
        timeLists = [0.080, 0.09]
    elif temp == 3:
        anglePath = [-16.0 * almath.TO_RAD, 0.0 * almath.TO_RAD]
        timeLists = [0.093, 0.107]

    isAbsolute = True
    motionProxy.angleInterpolation(names, anglePath, timeLists, isAbsolute)
    time.sleep(0.2)


def move_la(LSP, LSR, LEY, LER, LWY):

    # LWY = -2 * almath.TO_RAD
    # Initialize position of left Arm
    global z_offset_l
    names = ["LShoulderRoll", "LShoulderPitch","LElbowYaw", "LElbowRoll", "LWristYaw"]
    angles = [LSR, LSP + (z_offset_l * almath.TO_RAD),LEY, LER, LWY]  # Positive values make the arm go lower, negative: higher
    fractionMaxSpeed = 0.3
    motionProxy.setAngles(names, angles, fractionMaxSpeed)


def move_ra(RSP, RSR, REY, RER, RWY):

    # RWY = 2 * almath.TO_RAD
    # Initialize position of left Arm
    global z_offset_r
    names = ["RShoulderRoll", "RShoulderPitch", "RElbowYaw", "RElbowRoll", "RWristYaw"]
    angles = [RSR, RSP + (z_offset_r * almath.TO_RAD),REY, RER,RWY] # Positive values make the arm go lower, negative: higher
    fractionMaxSpeed = 0.3
    motionProxy.setAngles(names, angles, fractionMaxSpeed)


def move(note, bl, br):
    if note.startswith("l"):

        p = l_dict[note]
        move_la(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4])
        time.sleep(0.6)
        l_hit(bl)

    elif note.startswith("r"):

        p = r_dict[note]
        move_ra(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4])
        time.sleep(0.6)
        r_hit(br)
    else:
        time.sleep(0.5)


def ask_mallet():
    tts.say("Could you please give me the left stick?")
    time.sleep(0.2)

    LSR = 44 * almath.TO_RAD
    LSP = 75 * almath.TO_RAD
    LER = -44 * almath.TO_RAD
    LEY = -115 * almath.TO_RAD
    LWY = -30 * almath.TO_RAD
    LH = 50 * almath.TO_RAD

    names = ["LShoulderRoll", "LShoulderPitch", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]
    angles = [LSR, LSP, LEY, LER, LWY, LH]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    time.sleep(4.0)

    names = ["LHand"]
    angles = [10 * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(0.5)

    stiffness_on(motionProxy)
    motionProxy.setStiffnesses("Head", 1.0)
    motionProxy.setStiffnesses("LHand", 1.0)
    motionProxy.setStiffnesses("LArm", 1.0)
    # Initialize position of left Arm
    motionProxy.setStiffnesses("RHand", 1.0)
    motionProxy.setStiffnesses("RArm", 1.0)

    tts.say("Could you please give me the right stick?")
    time.sleep(0.2)

    RSR = -44 * almath.TO_RAD
    RSP = 75 * almath.TO_RAD
    RER = 44 * almath.TO_RAD
    REY = 115 * almath.TO_RAD
    RWY = 30 * almath.TO_RAD
    RH = 50 * almath.TO_RAD

    # Initialize position of left Arm
    names = ["RShoulderRoll", "RShoulderPitch", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angles = [RSR, RSP, REY, RER, RWY, RH]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(4.0)

    names = ["RHand"]
    angles = [10 * almath.TO_RAD]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(0.5)

    tts.say("Thank you.")
    time.sleep(0.2)


def l_arm_track(cx, cy, left_matrix, error_y):
    matrix2 = []

    y_dist = abs(cy) + 50.71 +17  # Offset between camera and torso frame approx 55 mm Variation between different robots
    x_dist = cx + 80 + error_y    # Mi note from the center of the metallophone = 80mm


    for i in range(0, len(left_matrix), 1):
        if int(y_dist) == int(left_matrix[i][0]):
            matrix2.append(left_matrix[i])

    if matrix2 == []:
        return matrix2, int(y_dist), int(x_dist)


    for j in range(0, len(matrix2), 1):
        # if int(l_cur_y) == int(matrix2[j][1]):
        if int(x_dist) == int(matrix2[j][1]):
            LSP = matrix2[j][2]
            LSR = matrix2[j][3]
            LEY = matrix2[j][4]
            LER = matrix2[j][5]
            # print "kinematics x, y: ",  matrix2[j][0],  matrix2[j][1]
            move_la(LSP, LSR, LEY, LER, +2* almath.TO_RAD)

    return matrix2, int(y_dist), int(x_dist)


def r_arm_track(cx, cy, right_matrix, error_y):
    matrix3 = []

    y_dist = abs(cy) + 50.71  +17  # Offset between camera and torso frame approx 55-60mm
    x_dist = cx - 80 + error_y     # Mi note from the center of the metallophone = 80mm

    for i in range(0, len(right_matrix), 1):
        if int(y_dist) == int(right_matrix[i][0]):
            matrix3.append(right_matrix[i])

    if matrix3 == []:
        return matrix3, int(y_dist), int(x_dist)

    for j in range(0, len(matrix3), 1):
        if int(x_dist) == int(matrix3[j][1]):
            RSP = matrix3[j][2]
            RSR = matrix3[j][3]
            REY = matrix3[j][4]
            RER = matrix3[j][5]
            move_ra(RSP, RSR, REY, RER, -2* almath.TO_RAD)


    return matrix3, int(y_dist), int(x_dist)


def best_hit():
    audio_levels = [0]

    global left_test
    global right_test

    best_left = 0
    best_right = 0
    best_laudio = 0
    best_raudio = 0
    case = 0
    for note in left_test:
        move(note, case, 0)
        time.sleep(0.2)
        audioLevel = aud.getFrontMicEnergy()
        print "audio level", audioLevel

        if audioLevel >= audio_levels[-1]:
            if audioLevel >= best_laudio:
                best_left = case
                best_laudio = audioLevel
        audio_levels.append(audioLevel)

        time.sleep(2.0)
        case += 1

    case = 0
    for note in right_test:
        move(note, 0, case)
        time.sleep(0.2)
        audioLevel = aud.getFrontMicEnergy()
        print "audio level", audioLevel
        if audioLevel >= audio_levels[-1]:
            if audioLevel >= best_raudio:
                best_raudio = audioLevel
                best_right = case
        audio_levels.append(audioLevel)

        time.sleep(2.0)
        case += 1

    return best_left, best_right  


def rest():
    tts.say("I need some rest, see you later.")
    time.sleep(0.2)

    LSR = 80 * almath.TO_RAD
    RSR = -80 * almath.TO_RAD
    LWY = -20 * almath.TO_RAD
    RWY = 20 * almath.TO_RAD
    LER = -80 * almath.TO_RAD
    RER = 80 * almath.TO_RAD

    names = ["LShoulderRoll", "RShoulderRoll", "LElbowRoll", "RElbowRoll", "LWristYaw", "RWristYaw"]
    angles = [LSR, RSR, LER, RER, LWY, RWY]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1.0)


    LSP = 50 * almath.TO_RAD
    RSP = 50 * almath.TO_RAD
    LER = -20 * almath.TO_RAD
    RER = 20 * almath.TO_RAD
    LSR = 30 * almath.TO_RAD
    RSR = -30 * almath.TO_RAD


    names = ["LShoulderPitch", "RShoulderPitch","LElbowRoll", "RElbowRoll","LShoulderRoll", "RShoulderRoll"]
    angles = [LSP, RSP,LER,RER,LSR,RSR]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1.0)

    LH = 50 * almath.TO_RAD
    RH = 50 * almath.TO_RAD

    names = ["LHand","RHand"]
    angles = [LH, RH]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1.0)

    LH = 20 * almath.TO_RAD
    RH = 20 * almath.TO_RAD

    names = ["LHand", "RHand"]
    angles = [LH, RH]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1.0)


    motionProxy.rest()

    sys.exit()


def define_notes(matrix2, matrix3):
    l_do = []
    l_re = []
    l_mi = []
    l_fa = []
    l_sol = []
    l_la = []

    r_do = []
    r_re = []
    r_mi = []
    r_fa = []
    r_sol = []
    r_si = []

    for i in range(0, 6):
        if i == 0:
            offset = 47
            for j in range(0, len(matrix2), 1):
                if int(l_cur_y + offset) == int(matrix2[j][1]):
                    LSP = matrix2[j][2]
                    LSR = matrix2[j][3]
                    LEY = matrix2[j][4]
                    LER = matrix2[j][5]
                    l_do.append([LSP, LSR, LEY, LER, 0])
                    # break
        elif i == 1:
            offset = 23
            for j in range(0, len(matrix2), 1):
                if int(l_cur_y + offset) == int(matrix2[j][1]):
                    LSP = matrix2[j][2]
                    LSR = matrix2[j][3]
                    LEY = matrix2[j][4]
                    LER = matrix2[j][5]
                    l_re.append([LSP, LSR, LEY, LER, 0])
                    # break
        elif i == 2:
            offset = 0
            for j in range(0, len(matrix2), 1):
                if int(l_cur_y + offset) == int(matrix2[j][1]):
                    LSP = matrix2[j][2]
                    LSR = matrix2[j][3]
                    LEY = matrix2[j][4]
                    LER = matrix2[j][5]
                    l_mi.append([LSP, LSR, LEY, LER, 0])
                    # break
        elif i == 3:
            offset = -25
            for j in range(0, len(matrix2), 1):
                if int(l_cur_y + offset) == int(matrix2[j][1]):
                    LSP = matrix2[j][2]
                    LSR = matrix2[j][3]
                    LEY = matrix2[j][4]
                    LER = matrix2[j][5]
                    l_fa.append([LSP, LSR, LEY, LER, 0])
                    # break
        elif i == 4:
            offset = -50
            for j in range(0, len(matrix2), 1):
                if int(l_cur_y + offset) == int(matrix2[j][1]):
                    LSP = matrix2[j][2]
                    LSR = matrix2[j][3]
                    LEY = matrix2[j][4]
                    LER = matrix2[j][5]
                    l_sol.append([LSP, LSR, LEY, LER, 0])
                    #     break
                    # else:
                    #
                    #     LSP = matrix2[0][2]
                    #     LSR = matrix2[0][3]
                    #     LEY = matrix2[0][4]
                    #     LER = matrix2[0][5]
                    #     l_sol.append([LSP, LSR, LEY, LER, 0])
        elif i == 5:
            offset = -71  #distance in mm
            for j in range(0, len(matrix2), 1):
                if int(l_cur_y + offset) == int(matrix2[j][1]):
                    LSP = matrix2[j][2]
                    LSR = matrix2[j][3]
                    LEY = matrix2[j][4]
                    LER = matrix2[j][5]
                    l_la.append([LSP, LSR, LEY, LER, 0])


    for i in range(0, 6):
        if i == 0:
            offset = -47
            for j in range(0, len(matrix3), 1):
                if int(r_cur_y + offset) == int(matrix3[j][1]):
                    RSP = matrix3[j][2]
                    RSR = matrix3[j][3]
                    REY = matrix3[j][4]
                    RER = matrix3[j][5]
                    r_sol.append([RSP, RSR, REY, RER, 0])
                    # break
        elif i == 1:
            offset = -25
            for j in range(0, len(matrix3), 1):
                if int(r_cur_y + offset) == int(matrix3[j][1]):
                    RSP = matrix3[j][2]
                    RSR = matrix3[j][3]
                    REY = matrix3[j][4]
                    RER = matrix3[j][5]
                    r_fa.append([RSP, RSR, REY, RER, 0])
        elif i == 2:
            offset = 0
            for j in range(0, len(matrix3), 1):
                if int(r_cur_y + offset) == int(matrix3[j][1]):
                    RSP = matrix3[j][2]
                    RSR = matrix3[j][3]
                    REY = matrix3[j][4]
                    RER = matrix3[j][5]
                    r_mi.append([RSP, RSR, REY, RER, 0])
                    # break
        elif i == 3:
            offset = 25
            for j in range(0, len(matrix3), 1):
                if int(r_cur_y + offset) == int(matrix3[j][1]):
                    RSP = matrix3[j][2]
                    RSR = matrix3[j][3]
                    REY = matrix3[j][4]
                    RER = matrix3[j][5]
                    r_re.append([RSP, RSR, REY, RER, 0])
                    # break
        elif i == 4:
            offset = 50
            for j in range(0, len(matrix3), 1):
                if int(r_cur_y + offset) == int(matrix3[j][1]):
                    RSP = matrix3[j][2]
                    RSR = matrix3[j][3]
                    REY = matrix3[j][4]
                    RER = matrix3[j][5]
                    r_do.append([RSP, RSR, REY, RER, 0])
                    # break
        elif i == 5:
            offset = 72
            for j in range(0, len(matrix3), 1):
                if int(r_cur_y + offset) == int(matrix3[j][1]):
                    RSP = matrix3[j][2]
                    RSR = matrix3[j][3]
                    REY = matrix3[j][4]
                    RER = matrix3[j][5]
                    r_si.append([RSP, RSR, REY, RER, 0])
                    # break
    return l_do, l_re, l_mi, l_fa, l_sol, l_la, r_do, r_re, r_mi, r_fa, r_sol, r_si


def check_shoulder_position():
    RSP = memProxy.getData("Device/SubDeviceList/RShoulderPitch/Position/Sensor/Value")
    LSP = memProxy.getData("Device/SubDeviceList/LShoulderPitch/Position/Sensor/Value")
    return RSP, LSP


def check_temp():
    RSP_temp = memProxy.getData("Device/SubDeviceList/RShoulderPitch/Temperature/Sensor/Status")
    LSP_temp = memProxy.getData("Device/SubDeviceList/LShoulderPitch/Temperature/Sensor/Status")
    RHR_temp = memProxy.getData("Device/SubDeviceList/RHipRoll/Temperature/Sensor/Status")
    LHR_temp = memProxy.getData("Device/SubDeviceList/LHipRoll/Temperature/Sensor/Status")
    RHP_temp = memProxy.getData("Device/SubDeviceList/RHipPitch/Temperature/Sensor/Status")
    LHP_temp = memProxy.getData("Device/SubDeviceList/LHipPitch/Temperature/Sensor/Status")

    # Status 0: ok
    # Status 1: motors are hot

    if (RSP_temp != 0 or LSP_temp != 0 or RHR_temp != 0 or LHR_temp != 0 or RHP_temp != 0 or LHP_temp != 0):
        rest()


def head_button():
    button1 = memProxy.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value")
    button2 = memProxy.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value")
    button3 = memProxy.getData("Device/SubDeviceList/Head/Touch/Rear/Sensor/Value")

    if (button1 == 1 or button2 == 1 or button3 == 1):
        return 1
    else:
        return 0


def check_matches():

    images = glob.glob('model_images/*.png')
    best_image = " "
    max_matches = 0

    for fname in images:
        img1 = cv2.imread(fname, 0)

        # img1 = cv2.imread('camImage.png', 0)  # queryImage
        img2 = cv2.imread('colored.png')  # trainImage

        gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(gray, (3, 3), 0)
        v = np.median(img)

        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - 0.33) * v))
        upper = int(min(255, (1.0 + 0.33) * v))
        edged = cv2.Canny(img, lower, upper)

        mask = cv2.erode(edged, None, iterations=0)
        img2 = cv2.dilate(mask, None, iterations=1)

        # Initiate SIFT detector
        sift = cv2.xfeatures2d.SIFT_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)

        # BFMatcher with default params
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        # Apply ratio test
        good = []
        for m, n in matches:
            if m.distance < 0.6 * n.distance:
                good.append(m)

        # Homography
        if len(good) > 25:
            query_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            train_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
            matches_mask = mask.ravel().tolist()

            # Perspective transform
            h, w = img1.shape
            pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
            dst = cv2.perspectiveTransform(pts, matrix)
            #
            # homography = cv2.polylines(img2, [np.int32(dst)], True, (255, 0, 0), 3)
            # #
            # cv2.imshow("Homography", homography)
            # cv2.waitKey(0)

            if len(good) >= max_matches:
                max_matches = len(good)
                best_image = str(fname)
        else:
            print "Not enough matches are found - %d/%d" % (len(good), 15)
            time.sleep(1)

    if best_image == " ":
        tts.say("I am sorry. I cannot see the metallophone, let's try again.")

        # motionProxy.rest()
        # sys.exit()
    else:
        return best_image


def get_image(IP, PORT):
    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    camera = 1  # 1 = bottom camera , 0 = top camera
    resolution = 2  # 2 = VGA
    colorSpace = 11  # RGB

    videoClient = camProxy.subscribeCamera("python_client", camera, resolution, colorSpace, 5)

    t0 = time.time()

    # Get a camera image.
    # image[6] contains the image data passed as an array of ASCII chars.
    naoImage = camProxy.getImageRemote(videoClient)

    t1 = time.time()

    camProxy.unsubscribe(videoClient)

    # Now we work with the image returned and save it as a PNG  using ImageDraw
    # package.

    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]
    im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
    im.save("headImage.png", "PNG")

##########################################
##  Functions used for visual servoing  ##
##########################################


def detect_error_left(x,y,z, rotation_vector, translation_vector):
    try:
        im = cv2.imread("headImage.png")
    except Exception, e:
        print "Could not read the image: ", e
        sys.exit()

    size = im.shape

    img = cv2.GaussianBlur(im, (3, 3), 0)
    v = np.median(img)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - 0.33) * v))
    upper = int(min(255, (1.0 + 0.33) * v))

    center = (size[1] / 2, size[0] / 2)

    # # ## V6
    camera_matrix = np.array(
        [[644.21806799, 0, center[0]],
         [0, 602.70821665, center[1]],
         [0, 0, 1]], dtype="double"
    )
    # V6 Robot
    dist_coeffs = np.array([0.16251826, -0.66618227, -0.00306388, 0.0056528, 0.68223892])

    ### Robot V5
    # camera_matrix = np.array(
    #     [[598.90793869, 0, center[0]],
    #      [0, 563.51165991, center[1]],
    #      [0, 0, 1]], dtype="double"
    # )
    # #### V5
    # dist_coeffs = np.array([-0.03725302, -0.01690297,  0.00335682, -0.00063561,  0.11640616])


    (l_mi_note, jacobian) = cv2.projectPoints(np.array([(-780.0, 0.0, 330.0)]), rotation_vector, translation_vector,
                                              camera_matrix, dist_coeffs)



    world_vect = np.zeros((3, 1))
    world_vect[0] = y
    world_vect[1] = z  # 209.3 -> 19
    world_vect[2] = x  # depth

    cam_rot_x = np.zeros((3, 3))
    cam_rot_x[0][0] = 1
    cam_rot_x[1][1] = math.cos(-140.3 * almath.TO_RAD) #39.7 degrees from x axis
    cam_rot_x[1][2] = - math.sin(-140.3 * almath.TO_RAD)
    cam_rot_x[2][1] = math.sin(-140.3 * almath.TO_RAD)
    cam_rot_x[2][2] = math.cos(-140.3 * almath.TO_RAD) #39.7 degrees from x axis

    vect = np.dot(cam_rot_x, world_vect)

    xy = np.dot(camera_matrix, vect)

    i_cam = np.linalg.inv(camera_matrix)
    i_rot = np.linalg.inv(cam_rot_x)


    xy[0] = xy[0] / xy[2]
    xy[1] = xy[1] / xy[2]
    xy[2] = xy[2] / xy[2]

    # print xy
    #
    x_s = int(xy[0] - 60)
    x_e = int(xy[0] + 180)
    if x_e >= 639:
        x_e = 639
    if x_s <= 0:
        x_s = 0

    y_s = int(xy[1] - 50)
    y_e = int(xy[1] + 200)
    if y_e >= 479:
        y_e = 479
    if y_s <=0:
        y_s = 0


    # print x_s, y_s, x_e, y_e

    if len(im.shape) > 2:
        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # param1 is the hiest value of canny edge param1=150
    circles = cv2.HoughCircles(im[y_s:y_e, x_s:x_e], cv2.HOUGH_GRADIENT, 1, 300, param1=upper, param2=10, minRadius=20,
                               maxRadius=40)
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(im, (x + x_s, y + y_s), r, (0, 255, 0), 4)
            cv2.rectangle(im, (x + x_s - 2, y + y_s - 2), (x + x_s + 2, y + y_s + 2), (0, 128, 255), -1)
            realx = x + x_s
            realy = y + y_s

    real2d = np.zeros((3, 1))
    real2d[0] = realx
    real2d[1] = realy
    real2d[2] = 1

    # print "real 2D:", real2d

    real3d_temp = np.dot(i_cam, real2d)

    real3d = np.dot(i_rot, real3d_temp)

    real3d[0] = real3d[0] * world_vect[2]
    real3d[1] = real3d[1] * world_vect[2]
    real3d[2] = real3d[2] * world_vect[2]
    # print "real 3D:", real3d
    im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
    # cv2.circle(im, (int(xy[0]), int(xy[1])), 30, (0, 255, 0), 4)


    cv2.circle(im, (int(l_mi_note[0][0][0]), int(l_mi_note[0][0][1])), 30, (0, 0, 255), 4)

    cv2.rectangle(im, (int(l_mi_note[0][0][0]) - 1, int(l_mi_note[0][0][1]) - 1),
                  (int(l_mi_note[0][0][0]) + 1, int(l_mi_note[0][0][1]) + 1), (0, 255, 0), 1)



    # cv2.imshow("Output", im)  # [78:194, 340:470]
    # cv2.waitKey(0)

    # error_y = world_vect[0] - abs(real3d[0])
    error_y = l_mi_note[0][0][0] - abs(real2d[0])


    error_z = l_mi_note[0][0][1] - real2d[1]

    # print "LEFT world - real: ", world_vect[1], abs(real3d[1])

    return error_y, error_z


def detect_error_right(x,y,z,rotation_vector, translation_vector):
    try:
        im = cv2.imread("headImage.png")
    except Exception, e:
        print "Could not read the image: ", e
        sys.exit()

    size = im.shape

    img = cv2.GaussianBlur(im, (3, 3), 0)
    v = np.median(img)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - 0.33) * v))
    upper = int(min(255, (1.0 + 0.33) * v))

    center = (size[1] / 2, size[0] / 2)
    ### Robot V6
    camera_matrix = np.array(
        [[644.21806799, 0, center[0]],
         [0, 602.70821665, center[1]],
         [0, 0, 1]], dtype="double"
    )
    # V6 Robot
    dist_coeffs = np.array([0.16251826, -0.66618227, -0.00306388, 0.0056528, 0.68223892])

    ## Robot V5
    # camera_matrix = np.array(
    #     [[598.90793869, 0, center[0]],
    #      [0, 563.51165991, center[1]],
    #      [0, 0, 1]], dtype="double"
    # )
    # #### V5
    # dist_coeffs = np.array([-0.03725302, -0.01690297,  0.00335682, -0.00063561,  0.11640616])


    (r_mi_note, jacobian) = cv2.projectPoints(np.array([(770.0, 0.0, 330.0)]), rotation_vector, translation_vector,
                                              camera_matrix, dist_coeffs)



    world_vect = np.zeros((3, 1))
    world_vect[0] = y -10 #
    world_vect[1] = z  # 209.3 -> 19
    world_vect[2] = x  # depth

    cam_rot_x = np.zeros((3, 3))
    cam_rot_x[0][0] = 1
    cam_rot_x[1][1] = math.cos(-140.3 * almath.TO_RAD) #39.7 degrees from x axis
    cam_rot_x[1][2] = - math.sin(-140.3 * almath.TO_RAD)
    cam_rot_x[2][1] = math.sin(-140.3 * almath.TO_RAD)
    cam_rot_x[2][2] = math.cos(-140.3 * almath.TO_RAD) #39.7 degrees from x axis

    vect = np.dot(cam_rot_x, world_vect)

    xy = np.dot(camera_matrix, vect)

    i_cam = np.linalg.inv(camera_matrix)
    i_rot = np.linalg.inv(cam_rot_x)


    xy[0] = xy[0] / xy[2]
    xy[1] = xy[1] / xy[2]
    xy[2] = xy[2] / xy[2]

    # print xy
    #
    x_s = int(xy[0] - 90)
    x_e = int(xy[0] + 180)
    if x_e >= 639:
        x_e = 639
    if x_s <= 0:
        x_s = 0

    y_s = int(xy[1] - 80)
    y_e = int(xy[1] + 200)
    if y_e >= 479:
        y_e = 479
    if y_s <=0:
        y_s = 0


    # print x_s, y_s, x_e, y_e

    if len(im.shape) > 2:
        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # param1 is the hiest value of canny edge param1=150
    circles = cv2.HoughCircles(im[y_s:y_e, x_s:x_e], cv2.HOUGH_GRADIENT, 1, 300, param1=upper, param2=10, minRadius=20,
                               maxRadius=40)
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(im, (x + x_s, y + y_s), r, (0, 255, 0), 4)
            cv2.rectangle(im, (x + x_s - 2, y + y_s - 2), (x + x_s + 2, y + y_s + 2), (0, 128, 255), -1)
            realx = x + x_s
            realy = y + y_s

    real2d = np.zeros((3, 1))
    real2d[0] = realx
    real2d[1] = realy
    real2d[2] = 1

    # print "real 2D:", real2d

    real3d_temp = np.dot(i_cam, real2d)

    real3d = np.dot(i_rot, real3d_temp)

    real3d[0] = real3d[0] * world_vect[2]
    real3d[1] = real3d[1] * world_vect[2]
    real3d[2] = real3d[2] * world_vect[2]
    # print "real 3D:", real3d

    im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
    # cv2.circle(im, (int(xy[0]), int(xy[1])), 30, (0, 255, 0), 4)



    cv2.circle(im, (int(r_mi_note[0][0][0]), int(r_mi_note[0][0][1])), 30, (0, 0, 255), 4)
    cv2.rectangle(im, (int(r_mi_note[0][0][0]) -1, int(r_mi_note[0][0][1])-1),
                  (int(r_mi_note[0][0][0])+1, int(r_mi_note[0][0][1])+1), (0, 255, 0), 1)

    # cv2.imshow("Output", im)
    # cv2.waitKey(0)
    # cv2.imwrite('headImage.png', im)


    # error_y = world_vect[0] + abs(real3d[0])
    error_y = r_mi_note[0][0][0] - abs(real2d[0])


    error_z = r_mi_note[0][0][1] - real2d[1]

    # print "RIGHT world - real: ", world_vect[1], abs(real3d[1])

    return error_y, error_z

##########################################################
###################### ~ MAIN ~ ##########################
##########################################################

start_time = time.time()

with open('config.txt') as data_file:
   data = json.loads(data_file.read())

robotIP = str(data["robotIP"])  # Change robotIP with the robot's IP
PORT = int(data["PORT"])             # Change PORT with the robot's PORT
state = 0

try:
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    aud = ALProxy("ALAudioDevice", robotIP, PORT)
    memProxy = ALProxy("ALMemory", robotIP, PORT)
except Exception, e:
        print "Could not create proxy, check if the robot's IP is correct"
        print "Error was: ", e

aud.enableEnergyComputation()

stiffness_on(motionProxy)
postureProxy.goToPosture("StandInit", 0.5)

doremi =['l_do','l_re', 'l_mi', 'l_fa', 'l_sol', 'l_la',
         'r_si','r_do', 'r_re','r_mi','r_fa','r_sol',]

left_test = ['l_mi', 'l_mi', 'l_mi', 'l_mi']
right_test = ['r_mi', 'r_mi', 'r_mi', 'r_mi']

#Jingle bells (Only left hand used)
jb = ['l_mi', 'l_mi', 'l_mi', 'pause', 'l_mi', 'l_mi', 'l_mi','pause', 'l_mi', 'l_sol', 'l_do', 'l_re',  'l_mi','pause', 'pause',
         'l_fa', 'l_fa', 'l_fa', 'l_fa', 'l_fa', 'l_mi', 'l_mi', 'l_mi', 'l_mi', 'l_mi',  'l_re', 'l_re',  'l_do', 'l_re', 'l_sol',
         'l_mi', 'l_mi', 'l_mi', 'pause', 'l_mi', 'l_mi', 'l_mi', 'pause', 'l_mi', 'l_sol', 'l_do', 'l_re', 'l_mi','pause', 'pause',
         'l_fa', 'l_fa', 'l_fa', 'l_fa', 'l_fa', 'l_mi', 'l_mi', 'l_mi', 'l_mi', 'l_sol','pause', 'l_sol','pause', 'l_fa','pause', 'l_re','pause','l_do']
#Happy birthday
happy_birth = ['l_do', 'l_do', 'l_re', 'l_do', 'l_fa', 'l_mi','pause',
              'l_do', 'l_do', 'l_re', 'l_do','l_sol',  'l_fa','pause',
              'l_do', 'l_do', 'r_do', 'l_la','pause', 'l_fa', 'l_mi', 'l_re','pause',
              'r_do', 'r_do', 'l_la', 'l_sol','pause', 'l_fa'
              ]
#Twinkle twinkle little star
twinkle = ['l_do', 'l_do', 'l_sol', 'l_sol', 'l_la', 'l_la','l_sol','pause',
              'l_fa', 'l_fa', 'l_mi', 'l_mi','l_re', 'l_re','l_do','pause',
              'l_sol', 'l_sol', 'l_fa', 'l_fa','l_mi', 'l_mi','l_re','pause',
              'l_sol', 'l_sol','l_fa', 'l_fa','l_mi', 'l_mi','l_re','pause',
              'l_do', 'l_do', 'l_sol', 'l_sol', 'l_la', 'l_la','l_sol','pause',
              'l_fa', 'l_fa', 'l_mi', 'l_mi','l_re', 'l_re','l_do',
              ]
#Ode to joy
ode_to_joy = ['l_mi', 'l_mi', 'l_fa', 'l_sol', 'l_sol', 'l_fa','l_mi',
              'l_re', 'l_do', 'l_do', 'l_re','l_mi','l_mi', 'l_re','l_re','pause',
              'l_mi', 'l_mi', 'l_fa', 'l_sol', 'l_sol', 'l_fa','l_mi',
              'l_re', 'l_do', 'l_do', 'l_re','l_mi','l_re', 'l_do','l_do','pause',
              'l_re', 'l_re', 'l_mi', 'l_do', 'l_re', 'l_mi', 'l_fa',
              'l_mi', 'l_do', 'l_re', 'l_mi', 'l_fa', 'l_mi', 'l_re', 'l_do','l_re', 'pause',
              'l_mi', 'l_mi', 'l_fa', 'l_sol', 'l_sol', 'l_fa', 'l_mi',
              'l_re', 'l_do', 'l_do', 'l_re', 'l_mi', 'l_re', 'l_do', 'l_do',
              ]
# The lion sleeps tonight
lion = ['l_sol', 'l_la', 'r_si', 'l_la', 'r_si', 'r_do', 'r_si', 'l_la', 'l_sol', 'l_la', 'r_si', 'l_la', 'l_sol',
        'r_si', 'l_la', 'pause', 'r_re', 'r_si', 'l_la', 'r_si', 'r_re', 'r_do', 'r_si', 'l_la', 'l_sol', 'l_la',
        'r_si', 'l_la', 'l_sol', 'r_si', 'l_la']


# Reading some songs from the user
text_file = open("song.txt", "r")
text_song = text_file.read().split(',')


user_song = {1:'l_do', 2:'l_re', 3:'l_mi', 4:'l_fa', 5:'l_sol', 6:'l_la', 7:'r_si', 8:'r_do', 9:'r_re', 10:'r_mi',
             11:'r_fa', 12:'r_sol', 13:'pause'}

text_song1 = []
for i in text_song:
    text_song1.append(user_song[int(i)])

# ask_mallet()      # Function ask_mallet wakes up the robot and make it ask for the mallets
# initial_pos()     # Function initial_pos put the arms into the initial state above the metallophone

try:
    left_matrix = np.loadtxt(open("Inverse/left_kine_test.csv", "rb"), delimiter=",", skiprows=0)
    right_matrix = np.loadtxt(open("Inverse/right_kine_test.csv", "rb"), delimiter=",", skiprows=0)
except IOError:
    print "Could not read pre-computed inverse kinematics files"
    sys.exit()

time.sleep(1.0)


tts.say("Hello! I need your help to play the metallophone.")
time.sleep(1)

tts.say("Now, place the metallophone in front of me. Approximately 5 centimeters from my body.")

time.sleep(5)

print "time.clock(): ", time.time() - start_time


#
# tts.say("I can play 5 songs. Please choose one.")
#
# song = 0
# while(song<1 or song>6):
#     song = input("Choose the song you want to play (1-6): ")
#
#
# play_switcher = {
#         1: jb,
#         2: happy_birth,
#         3: twinkle,
#         4: lion,
#         5: ode_to_joy,
#         6: text_song1
# }
# talk_switcher = {
#         1: "Jingle bells",
#         2: "Happy birthday",
#         3: "Twinkle twinkle little star",
#         4: "The lion sleeps tonight",
#         5: "Ode to joy",
#         6: "I am going to play your song"
# }
# string_to_speech = talk_switcher[song]
# tts.say(string_to_speech)
# tts.say("Great")

capture_image(robotIP, PORT)
time.sleep(1)

# loop for finding which model image fits best in the current environment
while(1):
    best_image = check_matches()
    if (best_image != " "):
        break

# best_image = 'model_images/model_image12.png'

print "task 1: ", time.time() - start_time , "seconds"

# loop for capturing images and estimating the pose of the metallophone
# In this phase a user must move the metallophone according to NAO's guidance
while(1):
    capture_image(robotIP, PORT)
    time.sleep(1.0)
    cx, cy, rot, rotation_vector, translation_vector = pose(best_image) # x and y distances between the camera and the center of metallophone in mm

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
      break

    print "cx: ", cx
    print "cy: ", cy
    l_error_y = 0
    r_error_y = 0

    check_temp()  # Always check motors' temperature for safety

    if (abs(cy) > 175):                                      # 175mm is a safe max distance (Could be a little bit more)
        tts.say("The metallophone is far away from me.")
        tts.say("Move it closer to me")
        state =0

    elif (abs(cy) < 160):                                   # 160mm is a safe min distance (Could be a little bit less)
        tts.say("The metallophone is too close to me")
        tts.say("Move it away from me")
        state = 0

    elif (cx < -10):                                         # cx is the distance between the center of the camera
                                                             #                  and the center of the metallophone
        tts.say("The metallophone is positioned too much to the right")
        tts.say("Move it to the left")
        state = 0

    elif (cx > 10):
        tts.say("The metallophone is positioned too much to the left")
        tts.say("Move it to the right")
        state = 0
    elif (rot > 10):
        tts.say("The metallophone is twisted to the right")
        tts.say("Rotate it to the left")
        state = 0
    elif (rot < -10):
        tts.say("The metallophone is twisted to the left")
        tts.say("Rotate it to the right")
        state = 0
    else:
        tts.say("Stop moving the metallophone. I can play.")
        state = state + 1

    if (state >= 2):
        tts.say("Touch my head button for 4 seconds to start.")

    time.sleep(3)
    button_state = head_button()
    if button_state == 1:
        state = 10
        print "task 2: ", time.time() - start_time, "seconds"

    global z_offset_l
    global z_offset_r

    z_offset_l = 0
    z_offset_r = 0

    l_error_y = 0
    r_error_y = 0
    r_error_z = 0
    l_error_z = 0
    y_offset_l = 0
    y_offset_r = 0
    if state == 10:


        ask_mallet()      # Function ask_mallet wakes up the robot and make it ask for the mallets

        initial_pos()  # Function initial_pos put the arms into the initial state above the metallophone

        print "task 3: ", time.time() - start_time, "seconds"

        matrix3, r_cur_x, r_cur_y = r_arm_track(cx, cy, right_matrix, r_error_y)
        time.sleep(2.0)
        matrix2, l_cur_x, l_cur_y = l_arm_track(cx, cy, left_matrix, l_error_y)
        time.sleep(2.0)

        capture_image(robotIP, PORT)
        time.sleep(2.0)

        cx, cy, rot, rotation_vector, translation_vector = pose(best_image)

        # Visual-Servoing phase

        for i in range(0, 6):               # In this loop we fix the error in the z-axis (right arm)
            get_image(robotIP, PORT)
            _, r_error_z = detect_error_right(abs(cy) + 50.71, cx - 80, 97, rotation_vector, translation_vector)

            if (abs(r_error_z) <= 18):
                break

            if (r_error_z > 0):
                z_offset_r = z_offset_r + 1

            if (r_error_z < 0):
                z_offset_r = z_offset_r - 1

            matrix3, r_cur_x, r_cur_y = r_arm_track(cx, cy, right_matrix, r_error_y)
            print "r_error_z: ", r_error_z


        for i in range(0, 6):                 # In this loop we fix the error in the z-axis (left arm)
            get_image(robotIP, PORT)
            _, l_error_z = detect_error_left(abs(cy) + 50.71, cx + 80, 97, rotation_vector, translation_vector)

            if (abs(l_error_z) <= 18):
                break

            if (l_error_z > 0):
                z_offset_l = z_offset_l + 1

            if (l_error_z < 0):
                z_offset_l = z_offset_l - 1

            matrix2, l_cur_x, l_cur_y = l_arm_track(cx, cy, left_matrix, l_error_y)
            # time.sleep(2.0)

            print "l_error_z: ", l_error_z


        for i in range(0, 20):            # In this loop we fix the error in the y-axis (right arm)

            get_image(robotIP, PORT)
            r_error_y, _ = detect_error_right(abs(cy) + 50.71, cx - 80, 97, rotation_vector, translation_vector)

            print "r_error_y: ", r_error_y

            if (abs(r_error_y) <= 8):
                break
            if (r_error_y > 0):
                y_offset_r = y_offset_r - 1

            if (r_error_y < 0):
                y_offset_r = y_offset_r + 1

            matrix3, r_cur_x, r_cur_y = r_arm_track(cx, cy, right_matrix, y_offset_r)
            # time.sleep(2.0)


        for i in range(0, 20):              # In this loop we fix the error in the y-axis (left arm)
            get_image(robotIP, PORT)
            l_error_y, _ = detect_error_left(abs(cy) + 50.71, cx + 80, 97, rotation_vector, translation_vector)

            print "l_error_y: ", l_error_y

            if (abs(l_error_y) <= 8):
                break
            if (l_error_y > 0):
                y_offset_l = y_offset_l - 2

            if (l_error_y < 0):
                y_offset_l = y_offset_l + 2

            matrix2, l_cur_x, l_cur_y = l_arm_track(cx, cy, left_matrix, y_offset_l)


        # Define the kinematics for all notes according to the initial position (Mi notes)
        l_do, l_re, l_mi, l_fa, l_sol, l_la, r_do, r_re, r_mi, r_fa, r_sol, r_si = define_notes(matrix2, matrix3)

        l_dict = {'l_do': l_do, 'l_re': l_re, 'l_mi': l_mi, 'l_fa': l_fa, 'l_sol': l_sol, 'l_la': l_la}
        r_dict = {'r_si': r_si, 'r_do': r_do, 'r_re': r_re, 'r_mi': r_mi, 'r_fa': r_fa, 'r_sol': r_sol}

        # Try 3 different hitting operatios in order to find the one with the most loud noise
        best_left, best_right = best_hit()
        print "best_left: ", best_left, "best_right", best_right

        # best_left = int(3)
        # best_right = int(3)

        tts.say("Let's play!")
        time.sleep(1.0)


        # for note in play_switcher[song]:
        #     move(note, best_left, best_right)
        #     time.sleep(0.2)
        # time.sleep(2.0)
        check_temp()
        #
        for note in doremi:
            move(note, best_left, best_right)
        time.sleep(2.0)
        check_temp()
        rest()

# End