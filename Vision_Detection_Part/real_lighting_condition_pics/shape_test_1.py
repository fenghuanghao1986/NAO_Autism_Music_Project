# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:13:15 2018

@author: fengh
"""
import cv2
import numpy as np
 
img = cv2.imread("1280.jpg", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 95, 100, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
font = cv2.FONT_HERSHEY_COMPLEX
 
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
 
    if len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
#    else:
#        cv2.putText(img, "Circle", (x, y), font, 1, (0))
 
cv2.imshow("shapes", img)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()