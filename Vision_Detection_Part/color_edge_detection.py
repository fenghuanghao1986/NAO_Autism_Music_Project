# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 10:41:57 2018

@author: CV_LAB_Howard
"""

# combined color and edge detection

import cv2
import numpy as np
# from matplotlib import pyplot as plt

# load the image
image = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\640.jpg')

# define the list of boundaries
boundaries = [
    ([0, 0, 100], [60, 60, 180]),     # red
    ([18, 43, 64], [40, 60, 86]),    # brown
    ([30, 140, 180], [60, 190, 240]),   # yellow
    ([20, 70, 50], [60, 110, 80]),     # green 
    ([100, 100, 120], [135, 134, 180]), # pink
    ([160, 120, 70], [210, 180, 130]),   # blue
    ([100, 135, 100], [155, 170, 160])  # gray 
]

n = 0

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    n = n + 1
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
 
	 # find the colors within the specified boundaries and apply
	 # the mask
    mask = cv2.inRange(image, lower, upper)
    
    output = cv2.bitwise_and(image, image, mask = mask)
    blurred = cv2.GaussianBlur(output, (3, 3), 0)
    
    # cv2.imshow("image", output)
    # show the images
    # cv2.imshow("images", np.hstack([image, output]))
    cv2.imwrite(str(n) + ".jpg", blurred)
    
    if n == 1:
        continue
    
    img = cv2.imread(str(n-1) + ".jpg")
    
    add = blurred + img
    cv2.imwrite(str(n) + ".jpg", add)

img = cv2.imread(str(n) + ".jpg", 1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (1, 1), 0)
# cv2.imshow("image", blurred)
result = cv2.Canny(blurred, 100, 225)  
# cv2.imshow("image", result)
# cv2.imshow("images", np.hstack([gray, result]))
compare = np.hstack([gray, result])
cv2.imwrite("edge.jpg", result)
cv2.imwrite("compare.jpg", compare)