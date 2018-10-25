# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:26:07 2018

@author: CV_LAB_Howard
"""
import cv2
import numpy as np

image = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\6.jpg')

center_blue = [[160, 120, 70], [210, 180, 130]]

for (lower, upper) in center_blue:
    # create NumPy arrays from the boundaries
    # n = n + 1
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
 
	 # find the colors within the specified boundaries and apply
	 # the mask
    mask = cv2.inRange(image, lower, upper)