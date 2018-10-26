# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:26:07 2018

@author: CV_LAB_Howard
"""
import cv2
import numpy as np

image = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\640b.jpg')

#center_blue = [[160, 120, 70], [210, 180, 130]]

def findBlue(img):
    
    result = []    
    print(img.shape)              
    height = img.shape[0]        
    width = img.shape[1]
    channels = img.shape[2]
    print("height:%s,width:%s,channels:%s" % (height,width,channels))
    print(img.size)              
    for row in range(height):    
        for col in range(width): 
            if img[row][col][0] >= 160 and img[row][col][0]<= 210:
                if img[row][col][1] >= 120 and img[row][col][1]<= 180:
                    if img[row][col][2] >= 70 and img[row][col][2]<= 130:
                        result.append((col, row))
    
    leftup = result[0]
    rightbottom = result[-1]
    cv2.rectangle(img, leftup, rightbottom, (0, 255, 0))
                   
    cv2.imshow("image",img) 

if __name__ == "__main__":
    findBlue(image)
    