# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:47:17 2018

@author: CV_LAB_Howard
"""
# import the necessary packages
import numpy as np

import cv2

# load the image
image = cv2.imread('xylophone_640_480.jpg')

# define the list of boundaries
boundaries = [
    ([0, 0, 200], [100, 100, 255]),     # red
    ([60, 70, 120], [100, 95, 160]),    # brown 
    ([30, 160, 240], [70, 255, 255]),   # yellow
    ([0, 130, 0], [120, 255, 150]),     # green 
    ([180, 100, 180], [255, 180, 255]), # pink
    ([200, 100, 0], [255, 255, 155]),   # blue
    ([192, 192, 192], [240, 240, 224])  # gray not good
]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
    
    