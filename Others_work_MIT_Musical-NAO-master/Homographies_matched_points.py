import cv2
import numpy as np
from matplotlib import pyplot as plt
from capture_image import capture_image
from PIL import Image
import time


# 2D points needed for 3D pose estimation. These points could be founded automatically with a color filter
im_points1 = np.float32([[107, 15], [41, 153], [529, 33], [560, 136]]).reshape(-1, 1, 2)  #1
im_points2 = np.float32([[113, 51], [44, 215], [570, 70], [617, 190]]).reshape(-1, 1, 2)  #2
im_points3 = np.float32([[103, 52], [28, 220], [571, 74], [617, 197]]).reshape(-1, 1, 2)  #3
im_points4 = np.float32([[118, 29], [52, 179], [562, 46], [604, 158]]).reshape(-1, 1, 2)  #4
im_points5 = np.float32([[111, 39], [45, 199], [564, 56], [610, 173]]).reshape(-1, 1, 2) #5
im_points6 = np.float32([[111, 38], [49, 191], [556, 50], [602, 165]]).reshape(-1, 1, 2) #6
im_points7 = np.float32([[106, 37], [34, 196], [565, 58], [603, 176]]).reshape(-1, 1, 2) #7
im_points8 = np.float32([[132, 24], [75, 168], [565, 42], [607, 147]]).reshape(-1, 1, 2) #8
im_points9 = np.float32([[115, 44], [48, 206], [576, 65], [623, 185]]).reshape(-1, 1, 2) #9
im_points10 = np.float32([[91, 35], [18, 199], [550, 54], [590, 176]]).reshape(-1, 1, 2) #10
im_points11 = np.float32([[78, 91], [3, 285], [575, 108], [630, 247]]).reshape(-1, 1, 2) #11
im_points12 = np.float32([[130, 85], [67, 233], [532, 106], [569, 212]]).reshape(-1, 1, 2) #12




points_dict = {"model_images/model_image1.png":im_points1, "model_images/model_image2.png":im_points2,
               "model_images/model_image3.png":im_points3, "model_images/model_image4.png":im_points4,
               "model_images/model_image5.png": im_points5, "model_images/model_image6.png":im_points6,
               "model_images/model_image7.png": im_points7, "model_images/model_image8.png":im_points8,
               "model_images/model_image9.png": im_points9,"model_images/model_image10.png": im_points10,
               "model_images/model_image11.png": im_points11, "model_images/model_image12.png": im_points12}


def track_points(img2, model):
    MIN_MATCH_COUNT = 15
    im_points = points_dict[model]

    img1 = cv2.imread(model, 0)  # queryImage (model image) came from main

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
        if m.distance < 0.7 * n.distance:
            good.append(m)

    # print "Matches: " , len(good)

    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)   # Calculate the homography matrix M

        # 2D points needed for 3D pose estimation.
        new_image_points = cv2.perspectiveTransform(im_points, M)  # Using M, transform the model points

        x_l = (new_image_points[0][0][0] + new_image_points[1][0][0]) / 2
        y_l = (new_image_points[0][0][1] + new_image_points[1][0][1]) / 2
        #
        x_r = (new_image_points[2][0][0] + new_image_points[3][0][0]) / 2
        y_r = (new_image_points[2][0][1] + new_image_points[3][0][1]) / 2

        image_points = np.zeros(shape=(5, 2), dtype="double")

        image_points[0] = [new_image_points[0][0][0], new_image_points[0][0][1]]
        image_points[1] = [new_image_points[1][0][0], new_image_points[1][0][1]]
        image_points[2] = [new_image_points[2][0][0], new_image_points[2][0][1]]
        image_points[3] = [new_image_points[3][0][0], new_image_points[3][0][1]]
        image_points[4] = [(x_l + x_r) / 2, (y_l + y_r) / 2]

        return image_points
    
    else:
        print "Not enough matches are found ", len(good), "out of ", MIN_MATCH_COUNT
        print "/n Try again in 2 seconds"
        time.sleep(2)

        default_points = np.zeros(shape=(5, 2), dtype="double")

        x_l = (im_points[0][0][0] + im_points[1][0][0]) / 2
        y_l = (im_points[0][0][1] + im_points[1][0][1]) / 2
        #
        x_r = (im_points[2][0][0] + im_points[3][0][0]) / 2
        y_r = (im_points[2][0][1] + im_points[3][0][1]) / 2

        default_points[0] = [im_points[0][0][0], im_points[0][0][1]]
        default_points[1] = [im_points[1][0][0], im_points[1][0][1]]
        default_points[2] = [im_points[2][0][0], im_points[2][0][1]]
        default_points[3] = [im_points[3][0][0], im_points[3][0][1]]
        default_points[4] = [(x_l + x_r) / 2, (y_l + y_r) / 2]

        return default_points
