# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:26:03 2018

@author: CV_LAB_Howard
"""

import cv2
import numpy as np

image = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\320b.jpg')

imgHLS = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

Lchannel = imgHLS[:,:,1]

mask = cv2.inRange(imgHLS, np.array([0,250,0]), np.array([255,255,255]))

res = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("image", res)