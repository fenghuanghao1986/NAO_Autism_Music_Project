# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:42:22 2018

@author: CV_LAB_Howard
"""

import cv2
import numpy as np

#image = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\320b.jpg')
video = r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\ideal_position_with_drum_stick_1.avi'


camera = cv2.VideoCapture(video)

counter = 0
out = cv2.VideoWriter('circle_test.avi', 
                      cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                      15, (320, 240))
while(True):
    
    (grabbed, frame) = camera.read()
        
    if grabbed == True:
            
        #frame = cv2.resize(frame, (320, 240))
        
        img = cv2.medianBlur(frame,3)
        cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#        edges = cv2.Canny(cimg,50,200)
        circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,15,5,
                                param1=100,param2=115,minRadius=5,maxRadius=15)
    
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
        
        cv2.imshow("Frame", frame)
        out.write(frame)
        key = cv2.waitKey(1) & 0xFF
        counter += 1
            
            # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break
            
    else:
        break
        
camera.release()
out.release()
cv2.destroyAllWindows()


