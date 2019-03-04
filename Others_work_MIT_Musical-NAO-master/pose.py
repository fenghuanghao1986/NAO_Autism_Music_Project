import cv2
import numpy as np
from naoqi import ALProxy
import almath
from PIL import Image
from capture_image import capture_image
import time
from Homographies_matched_points import track_points
import json
import math


def pose(model):
    
    # Read Image
    try:
        im = cv2.imread("colored.png")
    except Exception, e:
        print "Could not read the image: ", e
        sys.exit()

    size = im.shape

    # Image Processsing
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    filtered = cv2.GaussianBlur(gray, (3, 3), 0)
    v = np.median(filtered)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - 0.33) * v))
    upper = int(min(255, (1.0 + 0.33) * v))
    edges = cv2.Canny(filtered, lower, upper)
    im = cv2.dilate(edges, None, iterations=1)

    # 2D image points.
    im_points = track_points(im,model)

    # 3D model points.
    model_points = np.array([
        (-900.0, 450.0, 0.0),  # upper left x=9cm , y=4.5cm
        (-900.0, -450.0, .0),  # lower left x=9cm , y=4.5cm
        (900.0, 325.0, 0),  # upper right x=9cm, y= 3.5cm
        (900.0, -325.0, 0),  # lower right x=9cm, y= 3.5cm
        (0.0, 0.0, 0.0)  # center
    ])

    # Camera center
    center = (size[1] / 2, size[0] / 2)

    # #### Robot V6
    camera_matrix = np.array(
        [[644.21806799, 0, center[0]],
         [0, 602.70821665, center[1]],
         [0, 0, 1]], dtype="double"
    )
    #### V6 Robot
    dist_coeffs = np.array([0.16251826, -0.66618227, -0.00306388, 0.0056528, 0.68223892])


    ### Robot V5
    # camera_matrix = np.array(
    #     [[598.90793869, 0, center[0]],
    #      [0, 563.51165991, center[1]],
    #      [0, 0, 1]], dtype="double"
    # )
    # #### V5
    # dist_coeffs = np.array([-0.03725302, -0.01690297,  0.00335682, -0.00063561,  0.11640616])


    # 6-DOF pose estimation function
    (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, im_points, camera_matrix,
                                                                  dist_coeffs,
                                                                  flags=cv2.SOLVEPNP_ITERATIVE)

    # Transform rotation vector to rotation matrix
    rotation_matrix = cv2.Rodrigues(rotation_vector)[0]
    rotation_matrix_t = rotation_matrix.transpose()


    n_rotation_matrix_t = - rotation_matrix_t
    camera_pos = np.dot(n_rotation_matrix_t, translation_vector)  # Calculate the position of the camera

    # angles
    x = math.atan2(rotation_matrix[2][1], rotation_matrix[2][2])
    y = math.atan2(-rotation_matrix[2][0], math.sqrt((rotation_matrix[0][0]) * rotation_matrix[0][0]) + (
        rotation_matrix[1][0] * rotation_matrix[1][0]))
    z = math.atan2(rotation_matrix[1][0], rotation_matrix[0][0])

    # print math.degrees(x),math.degrees(y),math.degrees(z)

    cam_rot_x = np.zeros((3, 3))
    cam_rot_x[0][0] = 1
    cam_rot_x[1][1] = math.cos(-140.3 * almath.TO_RAD)  # 39.7 degrees from x axis
    cam_rot_x[1][2] = - math.sin(-140.3 * almath.TO_RAD)
    cam_rot_x[2][1] = math.sin(-140.3 * almath.TO_RAD)
    cam_rot_x[2][2] = math.cos(-140.3 * almath.TO_RAD)  # 39.7 degrees from x axis

    camera_pos1 = np.dot(cam_rot_x, translation_vector) # Calculate the position of the camera without
                                                        # taking into acount the rotations on y and z axes

    # print "Distance on x Axis: ", camera_pos[0] * 0.01, "cm"
    # print "Distance on y Axis: ", camera_pos[1] * 0.01, "cm"
    cx = -camera_pos1[0] * 0.1
    cy = camera_pos1[1] * 0.1
    cz = camera_pos[2] * 0.1

    # print "Distance on z Axis: ", camera_pos[2] * 0.01, "cm"


    (r_mi_note, jacobian) = cv2.projectPoints(np.array([(800.0, 0.0, 0.0)]), rotation_vector, translation_vector,
                                          camera_matrix, dist_coeffs)

    (l_mi_note, jacobian) = cv2.projectPoints(np.array([(-800.0, 0.0, 0.0)]), rotation_vector, translation_vector,
                                              camera_matrix, dist_coeffs)

    rot = int(r_mi_note[0][0][1]) - int(l_mi_note[0][0][1])

    print "rot: ", rot

    im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)

    # # #### Start !! Right MI note
    cv2.circle(im, (int(r_mi_note[0][0][0]), int(r_mi_note[0][0][1])), 5, (0, 0, 255), -1)

    # # #### Start !! Left MI note
    cv2.circle(im, (int(l_mi_note[0][0][0]), int(l_mi_note[0][0][1])), 5, (0, 0, 255), -1)

    # Draw the fixed cross on the screen
    cv2.line(im, (320,50), (320,250), (0, 255, 0), 2)
    cv2.line(im, (160,140), (480,140), (0, 255, 0), 2)
    count = 0
    for p in im_points:
        cv2.circle(im, (int(p[0]), int(p[1])), 5, (0, 0, 255), -1)
        im_points[count] = [p[0], p[1]]
        count += 1

    cv2.line(im, (int(r_mi_note[0][0][0]), int(r_mi_note[0][0][1])), (int(l_mi_note[0][0][0]), int(l_mi_note[0][0][1])), (0, 0, 255), 2)
    cv2.line(im, (int(im_points[4][0]), int(im_points[4][1]) - 40), (int(im_points[4][0]),int(im_points[4][1]) + 40), (0,0,255),2)

    cv2.imshow("Output", im)

    # print "cx, cy : ", cx, cy, cz
    return cx, cy, rot, rotation_vector, translation_vector