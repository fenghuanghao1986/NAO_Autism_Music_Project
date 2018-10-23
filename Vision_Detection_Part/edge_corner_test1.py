# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:05:10 2018

@author: fengh
"""

import cv2
import numpy as np


image = cv2.imread(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Vision_Detection_Part\7.jpg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = gray[270:, :] #cv2.GaussianBlur(gray, (3, 3), 0)
# cv2.imshow("image", blurred)
edge = cv2.Canny(blurred, 150, 300)
black = np.zeros((270, 640), dtype = int)
result = np.vstack((black, edge))
cv2.imshow("image", result)