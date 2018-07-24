# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:00:47 2018

@author: fengh
"""
import numpy as np
import cv2

print("1") 
img = cv2.imread('ball3.png',0)
print("2")
img = cv2.medianBlur(img,5)
print("3")
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print("4")
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,6,2000,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
print("5")
circles = np.uint16(np.around(circles))
print("6")
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()