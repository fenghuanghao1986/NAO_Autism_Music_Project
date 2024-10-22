# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np

img = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\2.jpg', 1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blurred = cv2.GaussianBlur(gray, (3, 3), 0)

result = cv2.Canny(gray, 100, 225)
result = np.float32(result) 
corner = cv2.cornerHarris(result,3,3,0.08) 
corner = cv2.dilate(corner, None)
img[corner>0.01*corner.max()]=[0,0,255]
cv2.imwrite("corner_img.jpg", img)
cv2.imshow("image", img)


