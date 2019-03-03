# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:12:08 2019

@author: CV_LAB_Howard
"""

import sys
import time
import cv2
import numpy as np

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import argparse

image = cv2.imread(r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\320b.jpg')

video = r'D:\Howard_Feng\noteDetection\Vision_Detection_Part\real_lighting_condition_pics\redball.avi'

#video = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Vision_Detection_Part\real_lighting_condition_pics\ideal_position_with_drum_stick_1.avi'
#blue = [[160, 120, 70], [210, 180, 130]]
#pink = [[100, 100, 120], [135, 134, 180]]
#gray = [[100, 135, 100], [155, 170, 160]]

class userColorMod(AlModule):
    def __init__(self, name):


    def updateVertices(vertices, centers, new_center):
            
        dx = new_center[0] - centers[5][0]
        dy = new_center[1] - centers[5][1]
        
        new_vertices = []
        for i in range(11):
            new_vertices.append([[vertices[i][0][0]+dx, vertices[i][0][1]+dy], 
                                 [vertices[i][1][0]+dx, vertices[i][1][1]+dy],
                                 [vertices[i][2][0]+dx, vertices[i][2][1]+dy],
                                 [vertices[i][3][0]+dx, vertices[i][3][1]+dy]])
        
        return new_vertices
    
    def updateCells(image):
        new_center = findBlueCenter(image)
        (vertices, centers) = initPos(image)
        new_vertices = updateVertices(vertices, centers, new_center)
        new_image = renderCells(image, new_vertices)  
        return new_image
        
        
    def initPos(image):
        vertices = []
        centers = []
        # initial left yellow position
        LU = [25, 141]
        RU = [40, 141]
        RB = [22, 187]
        LB = [3, 187]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
        '''cv2.polylines(image, [init_vertices], 1, (255, 255, 0))
        font       = cv2.FONT_HERSHEY_SIMPLEX
        centerText = centers[-1]
        fontScale  = 0.2
        fontColor  = (0,255,0)
        lineType   = 1
        cv2.putText(image,'F7', 
            centerText, 
            font, 
            fontScale,
            fontColor,
            lineType)'''
        # initial left red position
        LU = [50, 139]
        RU = [64, 139]
        RB = [50, 188]
        LB = [32, 188]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
    
        # initial left brown position
        LU = [75, 138]
        RU = [90, 138]
        RB = [80, 189]
        LB = [60, 189]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
    
        # initial green position
        LU = [100, 137]
        RU = [115, 137]
        RB = [108, 191]
        LB = [90, 191]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
    
        # initial pink position
        LU = [124, 135]
        RU = [140, 135]
        RB = [138, 192]
        LB = [119, 192]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
    
        # initial Blue position    
        LU = [149, 133]
        RU = [165, 133]
        RB = [167, 193]
        LB = [149, 193]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
    
        # initial gray position
        LU = [173, 131]
        RU = [188, 131]
        RB = [196, 195]
        LB = [178, 195]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
    
        # initial rignt yellow position
        LU = [197, 130]
        RU = [211, 130]
        RB = [226, 197]
        LB = [207, 197]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
    
        # initial rignt red position
        LU = [220, 129]
        RU = [234, 129]
        RB = [256, 199]
        LB = [236, 199]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
    
        # initial right brown position
        LU = [243, 127]
        RU = [257, 127]
        RB = [286, 200]
        LB = [266, 200]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)    
        vertices.append(init_vertices)
        centers.append(center)
    
        # initial right green position
        LU = [264, 125]
        RU = [277, 125]
        RB = [320, 202]
        LB = [297, 202]
        init = [LU, RU, RB, LB]
        init_vertices = np.array(init, dtype = np.int32)
        center = ((LU[0]+RU[0]+RB[0]+LB[0])/4, (LU[1]+RU[1]+RB[1]+LB[1])/4)
        vertices.append(init_vertices)
        centers.append(center)
        
        return (vertices, centers)
    
    def renderCells(image, vertices):
        for i in range(11):
            np_vertices = np.array(vertices[i], dtype = np.int32)
            cv2.polylines(image, [np_vertices], 1, (255, 255, 0))
        return image
    
    def findBlueCenter(img):
        sum_col = 0
        sum_row = 0
        avg_col = 0
        avg_row = 0
        center = (0,0)
        length = 0
                 
        height = img.shape[0]        
        width = img.shape[1]
                
        for row in range(height):   
            for col in range(width): 
                if img[row][col][0] >= 160 and img[row][col][0]<= 255: #155,255
                    if img[row][col][1] >= 120 and img[row][col][1]<= 180:
                        if img[row][col][2] >= 70 and img[row][col][2]<= 140:
                            sum_col += col
                            sum_row += row
                            length += 1
                            
        if length > 0:        
            avg_col = sum_col/length
            avg_row = sum_row/length
            
            center = (avg_col, avg_row+8)
        
        return center
        
    #def findBlue(image):
    #    
    #    img = cv2.GaussianBlur(image, (7, 7), 7)
    #    
    #    blue_result = []    
    ##    pink_result = []
    ##    gray_result = []
    #    
    #    sum_col = 0
    #    sum_row = 0
    #    avg_col = 0
    #    avg_row = 0
    #    
    #    print(img.shape)              
    #    height = img.shape[0]        
    #    width = img.shape[1]
    #    channels = img.shape[2]
    #    print("height:%s,width:%s,channels:%s" % (height,width,channels))
    #    print(img.size)              
    #    for row in range(height/2, height):   
    #        
    #        for col in range(width*2/6, width*4/6): 
    #            if img[row][col][0] >= 160 and img[row][col][0]<= 255: #155,255
    #                if img[row][col][1] >= 120 and img[row][col][1]<= 180:
    #                    if img[row][col][2] >= 70 and img[row][col][2]<= 140:
    #                        blue_result.append([col, row])
    #                        sum_col += col
    #                        sum_row += row
        
    #            if img[row][col][0] >= 120 and img[row][col][0]<= 140:
    #                if img[row][col][1] >= 120 and img[row][col][1]<= 130:
    #                    if img[row][col][2] >= 150 and img[row][col][2]<= 200:
    #                        pink_result.append([col, row])
                            
    #            if img[row][col][0] >= 140 and img[row][col][0]<= 160:
    #                if img[row][col][1] >= 140 and img[row][col][1]<= 160:
    #                    if img[row][col][2] >= 140 and img[row][col][2]<= 160:
    #                        gray_result.append([col, row])
                            
    #    if len(blue_result) > 0:
    #        print("array size:%d" % len(blue_result))
    #        pts = findVertices(blue_result)
    #        pts1 = np.array([pts[0], pts[1], pts[2], pts[3]], dtype = np.int32)  
    #        cv2.polylines(image, [pts1], 1, (255, 0, 0))
    #        
    #        avg_col = sum_col/len(blue_result)
    #        avg_row = sum_row/len(blue_result)
    #        
    #        new_center = (avg_col, avg_row)
        
    #        font                   = cv2.FONT_HERSHEY_SIMPLEX
    #        bottomLeftCornerOfText = (avg_col,avg_row)
    #        fontScale              = 0.2
    #        fontColor              = (0,255,0)
    #        lineType               = 1
    #        
    #        cv2.putText(image,'B', 
    #            bottomLeftCornerOfText, 
    #            font, 
    #            fontScale,
    #            fontColor,
    #            lineType)
                    
    #        width1 = pts[1][0] - pts[0][0]      
    ##        width2 = width1*5/4
    #        pts_pink = [[pts[0][0]-width1*8/5, pts[0][1]+width1/5], 
    #                    [pts[1][0]-width1*8/5, pts[1][1]+width1/5], 
    #                    [pts[2][0]-width1*10/5, pts[2][1]-width1/5], 
    #                    [pts[3][0]-width1*10/5, pts[3][1]-width1/5]]
    #        
    #        pts1_pink = np.array(pts_pink, dtype = np.int32)
    #        cv2.polylines(image, [pts1_pink], 1, (255, 0, 0))
    #        
    #        bottomLeftCornerOfText2 = (avg_col-2*width1,avg_row)
    #        
    #        cv2.putText(image,'P', 
    #            bottomLeftCornerOfText2, 
    #            font, 
    #            fontScale,
    #            fontColor,
    #            lineType)
    #        
    #    if len(pink_result) > 0:
    #        pts = findVertices(pink_result)
    #        pts1 = np.array([pts[0], pts[1], pts[2], pts[3]], dtype = np.int32)  
    #        cv2.polylines(image, [pts1], 1, (255, 255, 0))
            
    #    if len(gray_result) > 0:
    #        pts = findVertices(gray_result)
    #        pts1 = np.array([pts[0], pts[1], pts[2], pts[3]], dtype = np.int32)  
    #        cv2.polylines(image, [pts1], 1, (0, 0, 255))
    #        cv2.rectangle(image, leftup, rightbottom, (0,225,0))
    #        
    #    return (image, new_center)
                       
    
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
    
    #def findCircle(image):
    #    img = img
    #    # if it works then run the code next
    #        
    #    # img = cv2.imread(myWidget._image, 0)
    #    # img = cv2.imread('opencv_logo.png',0)
    #    Iimg = cv2.medianBlur(img,5)
    #    cimg = cv2.cvtColor(Iimg,cv2.COLOR_RGB2GRAY)
    #    
    #    circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,2,20000,
    #                               param1=50,param2=300,minRadius=0,maxRadius=0)
    #    
    #    circles = np.uint16(np.around(circles))
    #        for i in circles[0,:]:
    #            # draw the outer circle
    #            cv2.circle(Iimg,(i[0],i[1]),i[2],(0,255,0),2)
    #            # draw the center of the circle
    #            cv2.circle(Iimg,(i[0],i[1]),2,(0,0,255),3)
    #        
    #        #cv2.imshow('detected circles',cimg)
    #        #cv2.waitKey(0)
    #        #cv2.destroyAllWindows()
    #        qimg = CV2QImage(Iimg)
    #        
    #
    #        circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,6,2000,
    #                                    param1=50,param2=30,minRadius=0,maxRadius=0)
    #        if len(circles > 0):
    #            circles = np.uint16(np.around(circles))
    #            for i in circles[0,:]:
    #                # draw the outer circle
    #                cv2.circle(Iimg,(i[0],i[1]),i[2],(0,255,0),2)
    #                # draw the center of the circle
    #                cv2.circle(Iimg,(i[0],i[1]),2,(0,0,255),3)
    #            
    #            #cv2.imshow('detected circles',cimg)
    #            #cv2.waitKey(0)
    #            #cv2.destroyAllWindows()
    #            qimg = CV2QImage(Iimg)
#    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
 
#    if __name__ == '__main__' :
#        # Set up tracker.
#        # Instead of MIL, you can also use
#     
#        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
#        tracker_type = tracker_types[4]
#     
#        if int(minor_ver) < 3:
#            tracker = cv2.Tracker_create(tracker_type)
#        else:
#            if tracker_type == 'BOOSTING':
#                tracker = cv2.TrackerBoosting_create()
#            if tracker_type == 'MIL':
#                tracker = cv2.TrackerMIL_create()
#            if tracker_type == 'KCF':
#                tracker = cv2.TrackerKCF_create()
#            if tracker_type == 'TLD':
#                tracker = cv2.TrackerTLD_create()
#            if tracker_type == 'MEDIANFLOW':
#                tracker = cv2.TrackerMedianFlow_create()
#            if tracker_type == 'GOTURN':
#                tracker = cv2.TrackerGOTURN_create()
#            if tracker_type == 'MOSSE':
#                tracker = cv2.TrackerMOSSE_create()
#            if tracker_type == "CSRT":
#                tracker = cv2.TrackerCSRT_create()
#     
#        # Read video
#        video = cv2.VideoCapture("test_video_1.avi")
#     
#        # Exit if video not opened.
#        if not video.isOpened(): 
#            print "Could not open video"
#            sys.exit()
#     
#        # Read first frame.
#        ok, frame = video.read()
#        if not ok:
#            print 'Cannot read video file'
#            sys.exit()
#         
#        # Define an initial bounding box
#        bbox = (287, 23, 86, 320)
#     
#        # Uncomment the line below to select a different bounding box
#        bbox = cv2.selectROI(frame, False)
#     
#        # Initialize tracker with first frame and bounding box
#        ok = tracker.init(frame, bbox)
#     
#        while True:
#            # Read a new frame
#            ok, frame = video.read()
#            if not ok:
#                break
#             
#            # Start timer
#            timer = cv2.getTickCount()
#     
#            # Update tracker
#            ok, bbox = tracker.update(frame)
#     
#            # Calculate Frames per second (FPS)
#            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
#     
#            # Draw bounding box
#            if ok:
#                # Tracking success
#                p1 = (int(bbox[0]), int(bbox[1]))
#                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
#                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
#            else :
#                # Tracking failure
#                cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
#     
#            # Display tracker type on frame
#            cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
#         
#            # Display FPS on frame
#            cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
#     
#            # Display result
#            cv2.imshow("Tracking", frame)
#     
#            # Exit if ESC pressed
#            k = cv2.waitKey(1) & 0xff
#            if k == 27 : break
                
        
    def videoProcess(video):
        
        camera = cv2.VideoCapture(video)
        
        counter = 0
        
        out = cv2.VideoWriter('result_with_drum_stick.avi', 
                               cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                               15, (640, 480))
        while(True):
            (grabbed, frame) = camera.read()
            
            if grabbed == True:
                
                updated_frame = updateCells(frame)
                #frame = findBlue(frame)[0]
        #        frame = initPos(frame)[0]
                       # show the frame to our screen and increment the frame counter
                
                img = cv2.medianBlur(frame,3)
                cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(cimg,5,100)
                circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,10,5,
                                    param1=100,param2=120,minRadius=5,maxRadius=15)
        
                circles = np.uint16(np.around(circles))
                for i in circles[0,:]:
                    # draw the outer circle
                    cv2.circle(updated_frame,(i[0],i[1]),i[2],(0,255,0),2)
                    # draw the center of the circle
                    cv2.circle(updated_frame,(i[0],i[1]),2,(0,0,255),3)
            
                
                frame = cv2.resize(updated_frame, (640, 480))
                out.write(frame)
                cv2.imshow("Frame", frame)
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
          
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
# =============================================================================
#    parser.add_argument("--ip", type=str, default="127.0.0.1",
#                         help="Robot ip address")
# =============================================================================
# =============================================================================
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                         help="Robot ip address")
# =============================================================================
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
    
    #    img = cv2.resize(initPos(image)[0], (640, 480))
#    cv2.imshow("image", img)
#        
    # cleanup the camera and close any open windows
    videoProcess(video)