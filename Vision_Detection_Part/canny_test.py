# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:50:51 2018

@author: fengh
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\320b.jpg',0)
img = cv2.medianBlur(img,3)   
edges = cv2.Canny(img,50,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()