# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 23:26:41 2018

@author: fengh
"""

# -*- encoding: UTF-8 -*-
#
# This is a tiny example that shows how to show live images from Nao using PyQt.
# You must have python-qt4 installed on your system.
#

import sys

# from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPainter, QColor, qRed, qGreen, qBlue, qRgb, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication


from naoqi import ALProxy

# To get the constants relative to the video.
import vision_definitions

import cv2
import numpy as np

'''    
def QImageToMat(qimg):
    """RGB888"""
    #qimg = QImage()
    #qimg.load("/home/auss/Pictures/test.png")
    qimg = qimg.convertToFormat(QImage.Format_RGB888)
    qimg = qimg.rgbSwapped()
    #assert(qimg.byteCount() == qimg.width() * qimg.height() * 3)
    
    ptr = qimg.bits()
    # ptr.setsize(qimg.byteCount())
    arr = np.array(ptr)
    arr = np.resize(arr, qimg.byteCount())
    print(qimg.byteCount())
    mat = arr.reshape(qimg.height(), qimg.width(), 3)  #  Copies the data
    return mat 
'''

def QImage2CV(qimg):
    
    tmp = qimg
    
    cv_image = np.zeros((tmp.height(), tmp.width(), 3), dtype=np.uint8)
    
    for row in range(0, tmp.height()):
        for col in range(0, tmp.width()):
            r = qRed(tmp.pixel(col, row))
            g = qGreen(tmp.pixel(col, row))
            b = qBlue(tmp.pixel(col, row))
            cv_image[row,col,0] = r
            cv_image[row,col,1] = g
            cv_image[row,col,2] = b
    
    return cv_image

def CV2QImage(cv_image):
    
    width = cv_image.shape[1] 
    height = cv_image.shape[0]  
    
    pixmap = QPixmap(width, height) 
    qimg = pixmap.toImage()  
    
   
    for row in range(0, height):
        for col in range(0,width):
            r = cv_image[row,col,0]
            g = cv_image[row,col,1]
            b = cv_image[row,col,2]
            
            pix = qRgb(r, g, b)
            qimg.setPixel(col, row, pix)
    
    return qimg 


class ImageWidget(QWidget):
    """
    Tiny widget to display camera images from Naoqi.
    """
    def __init__(self, IP, PORT, CameraID, parent=None):
        """
        Initialization.
        """
        QWidget.__init__(self, parent)
        self._image = QImage()
        self.setWindowTitle('Nao')

        self._imgWidth = 320
        self._imgHeight = 240
        self._cameraID = CameraID
        self.resize(self._imgWidth, self._imgHeight)

        # Proxy to ALVideoDevice.
        self._videoProxy = None

        # Our video module name.
        self._imgClient = ""

        # This will contain this alImage we get from Nao.
        self._alImage = None

        self._registerImageClient(IP, PORT)

        # Trigget 'timerEvent' every 100 ms.
        self.startTimer(100)


    def _registerImageClient(self, IP, PORT):
        """
        Register our video module to the robot.
        """
        self._videoProxy = ALProxy("ALVideoDevice", IP, PORT)
        resolution = vision_definitions.kQVGA  # 320 * 240
        colorSpace = vision_definitions.kRGBColorSpace
        self._imgClient = self._videoProxy.subscribe("_client", resolution, colorSpace, 5)

        # Select camera.
        self._videoProxy.setParam(vision_definitions.kCameraSelectID,
                                  self._cameraID)


    def _unregisterImageClient(self):
        """
        Unregister our naoqi video module.
        """
        if self._imgClient != "":
            self._videoProxy.unsubscribe(self._imgClient)


    def paintEvent(self, event):
        """
        Draw the QImage on screen.
        """
        painter = QPainter(self)
        painter.drawImage(painter.viewport(), self._image)


    def _updateImage(self):
        """
        Retrieve a new image from Nao.
        """
        self._alImage = self._videoProxy.getImageRemote(self._imgClient)
        self._image = QImage(self._alImage[6],           # Pixel array.
                             self._alImage[0],           # Width.
                             self._alImage[1],           # Height.
                             QImage.Format_RGB888)


    def timerEvent(self, event):
        """
        Called periodically. Retrieve a nao image, and update the widget.
        """
        self._updateImage()
        # self.update()
        
        
        # first to see the details of this Qimage file
        # it should be a class type thing
        # then find the image which saved in Qimage
        img = QImage2CV(self._image)
        # if it works then run the code next
        
        # img = cv2.imread(myWidget._image, 0)
        # img = cv2.imread('opencv_logo.png',0)
        Iimg = cv2.medianBlur(img,5)
        cimg = cv2.cvtColor(Iimg,cv2.COLOR_RGB2GRAY)
        
        circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,6,20000,
                                    param1=50,param2=30,minRadius=0,maxRadius=0)
        if len(circles > 0):
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(Iimg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(Iimg,(i[0],i[1]),2,(0,0,255),3)
            
            #cv2.imshow('detected circles',cimg)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            qimg = CV2QImage(Iimg)
            
            self._image = qimg
            
            self.update()

    def __del__(self):
        """
        When the widget is deleted, we unregister our naoqi video module.
        """
        self._unregisterImageClient()


if __name__ == '__main__':
        
    IP = "169.254.254.250"  # Replace here with your NaoQi's IP address.
    PORT = 9559
    CameraID = 0

    # Read IP address from first argument if any.
    if len(sys.argv) > 1:
        IP = sys.argv[1]

    # Read CameraID from second argument if any.
    if len(sys.argv) > 2:
        CameraID = int(sys.argv[2])


    app = QApplication(sys.argv)
    myWidget = ImageWidget(IP, PORT, CameraID)
    myWidget.show()
    
    # img = myWidget._image
    
    sys.exit(app.exec_())




