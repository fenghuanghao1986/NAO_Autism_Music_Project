# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:50:51 2018

@author: fengh
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ball5.jpg',0)
   
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()