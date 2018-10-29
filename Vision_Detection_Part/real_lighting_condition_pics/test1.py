# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:26:07 2018

@author: CV_LAB_Howard
"""
import cv2
import numpy as np

image = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\t1.jpg')

#video = r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\test_video_1.avi'

video = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Vision_Detection_Part\real_lighting_condition_pics\test_video_1.avi'
#blue = [[160, 120, 70], [210, 180, 130]]
#pink = [[100, 100, 120], [135, 134, 180]]
#gray = [[100, 135, 100], [155, 170, 160]]

def findColor(image):
    
    img = cv2.GaussianBlur(image, (7, 7), 7)
    
    blue_result = []    
#    pink_result = []
#    gray_result = []
    
    sum_col = 0
    sum_row = 0
    avg_col = 0
    avg_row = 0
    
    print(img.shape)              
    height = img.shape[0]        
    width = img.shape[1]
    channels = img.shape[2]
    print("height:%s,width:%s,channels:%s" % (height,width,channels))
    print(img.size)              
    for row in range(height/2, height):    
        for col in range(width*2/6, width*4/6): 
            if img[row][col][0] >= 160 and img[row][col][0]<= 255: #155,255
                if img[row][col][1] >= 120 and img[row][col][1]<= 180:
                    if img[row][col][2] >= 70 and img[row][col][2]<= 140:
                        blue_result.append([col, row])
                        sum_col += col
                        sum_row += row
    
#            if img[row][col][0] >= 120 and img[row][col][0]<= 140:
#                if img[row][col][1] >= 120 and img[row][col][1]<= 130:
#                    if img[row][col][2] >= 150 and img[row][col][2]<= 200:
#                        pink_result.append([col, row])
#            if img[row][col][0] >= 140 and img[row][col][0]<= 160:
#                if img[row][col][1] >= 140 and img[row][col][1]<= 160:
#                    if img[row][col][2] >= 140 and img[row][col][2]<= 160:
#                        gray_result.append([col, row])
                        
    if len(blue_result) > 0:
        print("array size:%d" % len(blue_result))
        pts = findVertices(blue_result)
        pts1 = np.array([pts[0], pts[1], pts[2], pts[3]], dtype = np.int32)  
        cv2.polylines(image, [pts1], 1, (255, 0, 0))
        
        avg_col = sum_col/len(blue_result)
        avg_row = sum_row/len(blue_result)
    
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (avg_col,avg_row)
        fontScale              = 0.2
        fontColor              = (0,255,0)
        lineType               = 1
        
        cv2.putText(image,'B', 
            bottomLeftCornerOfText, 
            font, 
            fontScale,
            fontColor,
            lineType)
        
#        width1 = pts[1][0] - pts[0][0]
#        width2 = width1*5/4
#        pts_pink = [[pts[0][0]-width1*8/5, pts[0][1]+width1/4], 
#                    [pts[1][0]-width2*7/5, pts[1][1]+width1/5], 
#                    [pts[2][0]-width2*8/5, pts[2][1]-width1/5], 
#                    [pts[3][0]-width1*10/5, pts[3][1]-width1/5]]
#        pts1_pink = np.array(pts_pink, dtype = np.int32)
#        cv2.polylines(image, [pts1_pink], 1, (255, 0, 0))
#    if len(pink_result) > 0:
#        pts = findVertices(pink_result)
#        pts1 = np.array([pts[0], pts[1], pts[2], pts[3]], dtype = np.int32)  
#        cv2.polylines(image, [pts1], 1, (255, 255, 0))
#    if len(gray_result) > 0:
#        pts = findVertices(gray_result)
#        pts1 = np.array([pts[0], pts[1], pts[2], pts[3]], dtype = np.int32)  
#        cv2.polylines(image, [pts1], 1, (0, 0, 255))
#        cv2.rectangle(image, leftup, rightbottom, (0,225,0))
    return image
                   

def findVertices(pixs):
    
    leftup = pixs[0]
    rightbottom = pixs[-1]
    leftbottom = pixs[0]
    rightup = pixs[len(pixs)/2]
        
    for i in range(len(pixs)):
        if pixs[i][0] <= leftbottom[0] and pixs[i][1] >= leftbottom[1]:
            leftbottom = pixs[i]
        elif pixs[i][1] >= leftbottom[1] and pixs[i][0] >= leftbottom[0]:
            if pixs[i][1] - leftbottom[1] >= pixs[i][0] - leftbottom[0]:
                leftbottom = pixs[i]
                
    for i in range(len(pixs)/8):           
        if pixs[i][1] <= rightup[1] and pixs[i][0] >= rightup[0]:
            rightup = pixs[i]
        elif pixs[i][1] <= rightup[1] and pixs[i][0] <= rightup[0]:
            if rightup[1] - pixs[i][1] <= rightup[0] - pixs[i][0]:
                rightup = pixs[i]
                    
    print(leftup)
    print(leftbottom)
    print(rightbottom)
    print(rightup)
        
    return (leftup, rightup, rightbottom, leftbottom)
    
def videoProcess(video):
    camera = cv2.VideoCapture(video)
    
    counter = 0
    while(True):
        (grabbed, frame) = camera.read()
        frame = findColor(frame)
               # show the frame to our screen and increment the frame counter
        
        frame = cv2.resize(frame, (640, 480))
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        counter += 1
        
        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break
        
        
    camera.release()
    cv2.destroyAllWindows()
        
if __name__ == "__main__":
#    frame = cv2.resize(image, (640, 480))
#    cv2.imshow("image", findColor(frame))
    # cleanup the camera and close any open windows
    videoProcess(video)
    