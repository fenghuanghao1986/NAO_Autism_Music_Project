# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:42:22 2018

@author: CV_LAB_Howard
"""

import cv2
import numpy as np

#image = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\320b.jpg')

img = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\320b.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=200,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

