# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:23:32 2018

@author: CV_LAB_Howard
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\320b.jpg')
#rows,cols,ch = img.shape
#
#pts1 = np.float32([[50,50],[200,50],[50,200]])
#pts2 = np.float32([[10,100],[200,50],[100,250]])
#
#M = cv2.getAffineTransform(pts1,pts2)
#
#dst = cv2.warpAffine(img,M,(cols,rows))
#
#plt.subplot(121),plt.imshow(img),plt.title('Input')
#plt.subplot(122),plt.imshow(dst),plt.title('Output')
#plt.show()


rows,cols,ch = img.shape

pts1 = np.float32([[25, 141],[277, 125],[3, 187],[320, 202]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()