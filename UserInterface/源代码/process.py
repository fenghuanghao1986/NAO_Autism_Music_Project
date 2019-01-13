#Digital Image Process
#process.py
#By Li Zimian 5090379027
#Email: zerman@sjtu.edu.cn
#Algorithm of Digital Image Process
#Using OpenCV and Qt

#Actually, OpenCV doesn't have a struct of IplImage in Python. So I use cvMat.
from PyQt5 import QtGui
import cv2 as cv

class process:
    def __init__(self):
        self.use = 1
        
    #QImage To IplImage(cvMat)
    def QImageToIplImage(self,qImage,channel):
        width = qImage.width()
        height = qImage.height()
        IplImageBuffer = cv.CreateImage((width,height),8,channel)
        for y in range(height):
            for x in range(width):
                rgb = qImage.pixel(x,y)
                cv.Set2D(IplImageBuffer,y,x,
                         (QtGui.qRed(rgb),QtGui.qGreen(rgb),QtGui.qBlue(rgb)))
        return IplImageBuffer
    
    #IplImage(cvMat) To QImage
    def IplImageToQImage(self,iplImage):
        qImage = QtGui.QImage(iplImage.width,iplImage.height,
                             QtGui.QImage.Format_RGB32)
        mat = cv.GetMat(iplImage)
        for y in range(iplImage.height):
            for x in range(iplImage.width):
                red = int(mat[y,x][0])
                green = int(mat[y,x][1])
                blue = int(mat[y,x][2])
                qImage.setPixel(x,y,QtGui.qRgb(red,green,blue))
        return qImage
    
    #return gray histogram
    def grayImage(self,qImage):
        src = self.QImageToIplImage(qImage,1)
        width = src.width
        height = src.height
        mat = cv.GetMat(src)
        hist = []
        for i in range(256):
            hist.append(0)
        for i in range(height):
            for j in range(width):
                hist[int(mat[i,j])] = hist[int(mat[i,j])] + 1        
        maxNum = 0
        for i in range(256):
            if(hist[i] > maxNum):
                maxNum = hist[i]
        dst = cv.CreateImage((300,200),8,3)
        cv.Set(dst,cv.ScalarAll(255),None)
        width2 = float(dst.width)
        height2 = float(dst.height)
        binWidth = width2/256
        binUnith = height2/maxNum
        for i in range(256):
            #p0 = cv.cvPoint(i*binWidth,dst.height)
            #p1 = cv.cvPoint((i+1)*binWidth,dst.height - hist[i]*binUnith)
            cv.Rectangle(dst,(int(i*binWidth),int(height2)),
                         (int((i+1)*binWidth),int(height2 - hist[i]*binUnith)),cv.Scalar(0.5),-1,8,0)
        bufferQImage = self.IplImageToQImage(dst)
        return bufferQImage
    
    #return binary image
    def thresholdImage(self,qImage,value):
        src = self.QImageToIplImage(qImage,3)
        dst = cv.CloneImage(src)
        cv.Threshold(src,dst,value,255,cv.CV_THRESH_BINARY)
        qdst = self.IplImageToQImage(dst)
        return qdst
    
    #return resize image
    def resizeImage(self,qImage,width,height):
        src = self.QImageToIplImage(qImage,3)
        dst = cv.CreateImage((width,height),8,3)
        cv.Resize(src,dst)
        qdst = self.IplImageToQImage(dst)
        return qdst
        
    #return rotate image
    def rotateImage(self,qImage,angle):
        src = self.QImageToIplImage(qImage,3)
        dst = cv.CloneImage(src)
        rotMat = cv.CreateMat(2,3,cv.CV_32FC1)
        cv.GetRotationMatrix2D((src.width/2,src.height/2),angle,0.6,rotMat)
        cv.WarpAffine(src,dst,rotMat)
        qdst = self.IplImageToQImage(dst)
        return qdst

    #return robert image
    def sobelImage(self,qImage):
        dst = QtGui.QImage(qImage)
        for i in range(dst.width()-1):
            for j in range(dst.height()-1):
                r = QtGui.qRed(dst.pixel(i+1,j+1)) - QtGui.qRed(dst.pixel(i,j))
                g = QtGui.qGreen(dst.pixel(i+1,j+1)) - QtGui.qGreen(dst.pixel(i,j))
                b = QtGui.qBlue(dst.pixel(i+1,j+1)) - QtGui.qBlue(dst.pixel(i,j))
                if(r < 0):
                    r = 0
                if(g < 0):
                    g = 0
                if(b < 0):
                    b = 0
                dst.setPixel(i,j,QtGui.qRgb(r,g,b))
        return dst

    #return Gaussian image
    def gaussImage(self,qImage):
        src = self.QImageToIplImage(qImage,3)
        dst = cv.CloneImage(src)
        cv.Smooth(src,dst,cv.CV_GAUSSIAN)
        qdst = self.IplImageToQImage(dst)
        return qdst

    #return Median image
    def medianImage(self,qImage):
        src = self.QImageToIplImage(qImage,3)
        dst = cv.CloneImage(src)
        cv.Smooth(src,dst,cv.CV_MEDIAN)
        qdst = self.IplImageToQImage(dst)
        return qdst
