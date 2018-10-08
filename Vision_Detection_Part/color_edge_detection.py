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
image = cv2.imread('xylophone_640_480.jpg')

# define the list of boundaries
boundaries = [
    ([0, 0, 200], [100, 100, 255]),     # red
    ([40, 50, 120], [100, 90, 160]),    # brown
    ([30, 160, 240], [70, 255, 255]),   # yellow
    ([0, 130, 0], [120, 255, 150]),     # green 
    ([180, 100, 180], [255, 180, 255]), # pink
    ([200, 100, 0], [255, 255, 155]),   # blue
    ([192, 192, 192], [240, 240, 224])  # gray 
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
    blurred = cv2.GaussianBlur(output, (5, 5), 0)
    
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
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
# cv2.imshow("image", blurred)
result = cv2.Canny(blurred, 100, 225)  
# cv2.imshow("image", result)
cv2.imshow("images", np.hstack([gray, result]))
compare = np.hstack([gray, result])
cv2.imwrite("edge.jpg", result)
cv2.imwrite("compare.jpg", compare)