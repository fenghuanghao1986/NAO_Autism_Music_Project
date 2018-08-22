# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:50:51 2018

@author: fengh
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ball5.jpg',0)

# set blue thresh
lower_blue=np.array([78,43,46])
upper_blue=np.array([110,255,255])

# change to hsv model
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# get mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow('Mask', mask)

# detect blue
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Result', res)
    
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()