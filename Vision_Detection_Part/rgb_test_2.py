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
    ([70, 80, 130], [120, 120, 190]),     # brown not good
    ([30, 160, 240], [70, 255, 255]),   # yellow
    ([100, 165, 0], [150, 200, 150]),  # green not good
    ([180, 100, 180], [255, 180, 255]), # pink
    ([200, 100, 0], [255, 255, 155]),   # blue
    ([210, 210, 210], [230, 230, 230])  # gray not good
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
    
    