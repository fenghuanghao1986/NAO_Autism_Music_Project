# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:56:46 2018

@author: CV_LAB_Howard
"""

import sys

from naoqi import ALProxy

# To get the constants relative to the video.
import vision_definitions

import cv2
import numpy as np

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
        # painter = QPainter(self)
        # painter.drawImage(painter.viewport(), self._image)


    def _updateImage(self):
        """
        Retrieve a new image from Nao.
        """
#        self._alImage = self._videoProxy.getImageRemote(self._imgClient)
#        self._image = QImage(self._alImage[6],           # Pixel array.
#                             self._alImage[0],           # Width.
#                             self._alImage[1],           # Height.
#                             QImage.Format_RGB888)


    def timerEvent(self, event):
        """
        Called periodically. Retrieve a nao image, and update the widget.
        """
        self._updateImage()
        self.update()
       
       
    def __del__(self):
        """
        When the widget is deleted, we unregister our naoqi video module.
        """
        self._unregisterImageClient()



import numpy as np
import cv2
import time
import requests
import threading
from threading import Thread, Event, ThreadError

class Cam():

  def __init__(self, url):
    
    self.stream = requests.get(url, stream=True)
    self.thread_cancelled = False
    self.thread = Thread(target=self.run)
    print "camera initialised"

    
  def start(self):
    self.thread.start()
    print "camera stream started"
    
  def run(self):
    bytes=''
    while not self.thread_cancelled:
      try:
        bytes+=self.stream.raw.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
          jpg = bytes[a:b+2]
          bytes= bytes[b+2:]
          img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
          cv2.imshow('cam',img)
          if cv2.waitKey(1) ==27:
            exit(0)
      except ThreadError:
        self.thread_cancelled = True
        
        
  def is_running(self):
    return self.thread.isAlive()
      
    
  def shut_down(self):
    self.thread_cancelled = True
    #block while waiting for thread to terminate
    while self.thread.isAlive():
      time.sleep(1)
    return True

  
    
#if __name__ == "__main__":
#  url = 'http://192.168.2.1/?action=stream'
#  cam = Cam(url)
#  cam.start()




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
    

    sys.exit(app.exec_())

#    # img = myWidget._image
#    # first to see the details of this Qimage file
#    # it should be a class type thing
#    # then find the image which saved in Qimage
#    # img = QImageToMat(._image)
#    # if it works then run the code next
#        
#    img = cv2.imread(myWidget._image, 0)
#    # img = cv2.imread('opencv_logo.png',0)
#    Iimg = cv2.medianBlur(img,5)
#    cimg = cv2.cvtColor(Iimg,cv2.COLOR_GRAY2BGR)
#        
#    circles = cv2.HoughCircles(Iimg,cv2.HOUGH_GRADIENT,1,20,
#                                    param1=50,param2=30,minRadius=0,maxRadius=0)
#        
#    circles = np.uint16(np.around(circles))
#    for i in circles[0,:]:
#        # draw the outer circle
#        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#        # draw the center of the circle
#        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
#        
#    #cv2.imshow('detected circles',cimg)
#    #cv2.waitKey(0)
#    #cv2.destroyAllWindows()