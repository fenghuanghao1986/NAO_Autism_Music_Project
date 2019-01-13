# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DIP.ui'
#
# Created: Tue May 08 22:18:52 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from process import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(parent)
        self.currentImage = QtGui.QImage()
        self.currentFilename = ""
        self.actionOpen.triggered.connect(self.showOpen)
        self.actionSave.triggered.connect(self.showSave)
        self.actionCancel.triggered.connect(self.showCancel)
        self.pushButton.clicked.connect(self.showThreshold)
        self.pushButton_2.clicked.connect(self.showResize)
        self.pushButton_3.clicked.connect(self.showRotate)
        self.pushButton_4.clicked.connect(self.showSobel)
        self.pushButton_5.clicked.connect(self.showGauss)
        self.pushButton_6.clicked.connect(self.showMedian)
        '''
        self.connect(self.actionOpen,QtCore.SIGNAL('triggered()'),self.showOpen)
        self.connect(self.actionSave,QtCore.SIGNAL('triggered()'),self.showSave)
        self.connect(self.actionCancel,QtCore.SIGNAL('triggered()'),self.showCancel)
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.showThreshold)
        self.connect(self.pushButton_2,QtCore.SIGNAL('clicked()'),self.showResize)
        self.connect(self.pushButton_3,QtCore.SIGNAL('clicked()'),self.showRotate)
        self.connect(self.pushButton_4,QtCore.SIGNAL('clicked()'),self.showSobel)
        self.connect(self.pushButton_5,QtCore.SIGNAL('clicked()'),self.showGauss)
        self.connect(self.pushButton_6,QtCore.SIGNAL('clicked()'),self.showMedian)
        '''
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalSlider = QtWidgets.QSlider(self.tab_3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider.setRange(0,255)
        self.horizontalSlider.setPageStep(1)
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_6.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setRange(0,10000)
        self.spinBox.setValue(0)
        self.spinBox.setSingleStep(10)
        self.gridLayout_5.addWidget(self.spinBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_2.setRange(0,10000)
        self.spinBox_2.setValue(0)
        self.spinBox_2.setSingleStep(10)
        self.gridLayout_5.addWidget(self.spinBox_2, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_5.addWidget(self.pushButton_2, 2, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_3.setRange(0,360)
        self.spinBox_3.setValue(0)
        self.spinBox_3.setSingleStep(1)
        self.gridLayout_4.addWidget(self.spinBox_3, 0, 2, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton.setChecked(True)
        self.gridLayout_4.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_4.addWidget(self.radioButton_2, 1, 1, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_4.addWidget(self.pushButton_3, 2, 0, 1, 3)
        self.gridLayout_3.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_7.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_7.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget_2, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 362, 492))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionCancel = QtWidgets.QAction(MainWindow)
        self.actionCancel.setObjectName(_fromUtf8("actionCancel"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionCancel)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "DIP", None))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "DO", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "Histogram Analysis", None))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Convolution", None))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "Robert Operator", None))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Geometric Operation", None))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Resize", None))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Height", None))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Width", None))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "DO", None))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "Rotate", None))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Angle", None))
        self.radioButton.setText(QtWidgets.QApplication.translate("MainWindow", "Clockwise", None))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Counter-clockwise", None))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "DO", None))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Filters", None))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "Gaussian filter", None))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "Median filter ", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtWidgets.QApplication.translate("MainWindow", "Options and Filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Tab 1", None))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None))
        self.actionCancel.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None))

    def showGray(self):
        grayImage = QtGui.QImage()
        proc = process()
        grayImage = proc.grayImage(self.currentImage)
        scene = QtWidgets.QGraphicsScene()
        scene.clear()
        scene.addPixmap(QtGui.QPixmap.fromImage(grayImage))
        self.graphicsView.setScene(scene)
        
    def showOpen(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', QtCore.QDir.currentPath(),"Images (*.jpg *.png *.bmp );;All files(*.*)")
        if not(filename.isNull()):
            image = QtGui.QImage()
            image.load(filename)
            self.originImage = image                     
            self.currentImage = image
            self.currentFilename = filename
            newScrollArea = QtWidgets.QScrollArea(self.tab)
            imageLabel = QtWidgets.QLabel(newScrollArea)
            imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.currentImage))
            newScrollArea.setWidget(imageLabel)
            self.tabWidget.addTab(newScrollArea,self.currentFilename)
            self.tabWidget.removeTab(0)
            self.showGray()
            self.spinBox.setValue(self.currentImage.height())
            self.spinBox_2.setValue(self.currentImage.width())

    def showSave(self):
        qpath = QtCore.QDir.currentPath()
        qfilename = QtCore.QString(self.currentFilename)
        qdir = qpath + qfilename
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save file', qdir,"Images (*.jpg *.png *.bmp );;All files(*.*)")
        if not(filename.isNull()):
           image = QtGui.QImage(self.currentImage)
           image.save(filename)
        
    def showThreshold(self):
        value = self.horizontalSlider.value()
        proc = process()
        newImage = QtGui.QImage()
        newImage = proc.thresholdImage(self.currentImage,value)
        self.currentImage = newImage
        newScrollArea = QtGui.QScrollArea(self.tab)
        imageLabel = QtGui.QLabel(newScrollArea)
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.currentImage))
        newScrollArea.setWidget(imageLabel)
        self.tabWidget.addTab(newScrollArea,self.currentFilename)
        self.tabWidget.removeTab(0)
        self.showGray()
        self.spinBox.setValue(self.currentImage.height())
        self.spinBox_2.setValue(self.currentImage.width())
        
    def showResize(self):
        height = self.spinBox.value()
        width = self.spinBox_2.value()
        proc = process()
        newImage = QtGui.QImage()
        newImage = proc.resizeImage(self.currentImage,width,height)
        self.currentImage = newImage
        newScrollArea = QtGui.QScrollArea(self.tab)
        imageLabel = QtGui.QLabel(newScrollArea)
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.currentImage))
        newScrollArea.setWidget(imageLabel)
        self.tabWidget.addTab(newScrollArea,self.currentFilename)
        self.tabWidget.removeTab(0)
        self.showGray()
        self.spinBox.setValue(self.currentImage.height())
        self.spinBox_2.setValue(self.currentImage.width())
        
    def showRotate(self):
        if(self.radioButton.isChecked()):
            angle = self.spinBox_3.value()
        elif (self.radioButton_2.isChecked()):
            angle = -self.spinBox_3.value()
        proc = process()
        newImage = QtGui.QImage()
        newImage = proc.rotateImage(self.currentImage,angle)
        self.currentImage = newImage
        newScrollArea = QtGui.QScrollArea(self.tab)
        imageLabel = QtGui.QLabel(newScrollArea)
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.currentImage))
        newScrollArea.setWidget(imageLabel)
        self.tabWidget.addTab(newScrollArea,self.currentFilename)
        self.tabWidget.removeTab(0)
        self.showGray()
        self.spinBox.setValue(self.currentImage.height())
        self.spinBox_2.setValue(self.currentImage.width())
        
    def showSobel(self):
        proc = process()
        newImage = QtGui.QImage()
        newImage = proc.sobelImage(self.currentImage)
        self.currentImage = newImage
        newScrollArea = QtGui.QScrollArea(self.tab)
        imageLabel = QtGui.QLabel(newScrollArea)
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.currentImage))
        newScrollArea.setWidget(imageLabel)
        self.tabWidget.addTab(newScrollArea,self.currentFilename)
        self.tabWidget.removeTab(0)
        self.showGray()
        self.spinBox.setValue(self.currentImage.height())
        self.spinBox_2.setValue(self.currentImage.width())

    def showGauss(self):
        proc = process()
        newImage = QtGui.QImage()
        newImage = proc.gaussImage(self.currentImage)
        self.currentImage = newImage
        newScrollArea = QtGui.QScrollArea(self.tab)
        imageLabel = QtGui.QLabel(newScrollArea)
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.currentImage))
        newScrollArea.setWidget(imageLabel)
        self.tabWidget.addTab(newScrollArea,self.currentFilename)
        self.tabWidget.removeTab(0)
        self.showGray()
        self.spinBox.setValue(self.currentImage.height())
        self.spinBox_2.setValue(self.currentImage.width())

    def showMedian(self):
        proc = process()
        newImage = QtGui.QImage()
        newImage = proc.medianImage(self.currentImage)
        self.currentImage = newImage
        newScrollArea = QtGui.QScrollArea(self.tab)
        imageLabel = QtGui.QLabel(newScrollArea)
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.currentImage))
        newScrollArea.setWidget(imageLabel)
        self.tabWidget.addTab(newScrollArea,self.currentFilename)
        self.tabWidget.removeTab(0)
        self.showGray()
        self.spinBox.setValue(self.currentImage.height())
        self.spinBox_2.setValue(self.currentImage.width())

    def showCancel(self):
        self.currentImage = self.originImage
        newScrollArea = QtGui.QScrollArea(self.tab)
        imageLabel = QtGui.QLabel(newScrollArea)
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.currentImage))
        newScrollArea.setWidget(imageLabel)
        self.tabWidget.addTab(newScrollArea,self.currentFilename)
        self.tabWidget.removeTab(0)
        self.showGray()
        self.spinBox.setValue(self.currentImage.height())
        self.spinBox_2.setValue(self.currentImage.width())
