# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:26:07 2018

@author: CV_LAB_Howard
"""
import cv2
import numpy as np

image1 = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\640b.jpg')
image2 = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\cornerb.jpg')

minus = image1 - image2

cv2.imshow("image", minus)