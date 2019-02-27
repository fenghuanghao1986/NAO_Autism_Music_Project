# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student_Music_Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from subwindow import *
import sounddevice as sd
import soundfile as sf

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.currentWindow = None
        self.win = None
        self.setupUi(parent)
        self.pushButton.clicked.connect(self.showSubWindow0)
        self.pushButton_2.clicked.connect(self.showSubWindow1)
        self.pushButton_3.clicked.connect(self.showSubWindow2)
        self.pushButton_4.clicked.connect(self.showSubWindow3)
        self.pushButton_5.clicked.connect(self.showSubWindow4)
        self.pushButton_6.clicked.connect(self.showSubWindow5)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1369, 901)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 80, 991, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 160, 180, 160))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 160, 180, 160))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 380, 180, 160))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(940, 380, 180, 160))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 380, 180, 160))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 160, 180, 160))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1369, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
    
    def process(self, filename):
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        sd.wait()
    
    def showSubWindow0(self, MainWindow):
            self.process(r"D:\Howard_Feng\noteDetection\UserInterface\music_annotation_ui\a.WAV")
            self.currentWindow = QtWidgets.QMainWindow()
            self.win = Ui_SubWindow(self.currentWindow)
            self.win.setMusicId(0)
            self.currentWindow.show()

    def showSubWindow1(self, MainWindow):
            self.process(r"D:\Howard_Feng\noteDetection\UserInterface\music_annotation_ui\c.WAV")
            self.currentWindow = QtWidgets.QMainWindow()
            self.win = Ui_SubWindow(self.currentWindow)
            self.win.setMusicId(1)
            self.currentWindow.show()
            
    def showSubWindow2(self, MainWindow):
            self.process(r"D:\Howard_Feng\noteDetection\UserInterface\music_annotation_ui\e.WAV")
            self.currentWindow = QtWidgets.QMainWindow()
            self.win = Ui_SubWindow(self.currentWindow)
            self.win.setMusicId(2)
            self.currentWindow.show()

    def showSubWindow3(self, MainWindow):
            self.process(r"D:\Howard_Feng\noteDetection\UserInterface\music_annotation_ui\g.WAV")
            self.currentWindow = QtWidgets.QMainWindow()
            self.win = Ui_SubWindow(self.currentWindow)
            self.win.setMusicId(3)
            self.currentWindow.show()

    def showSubWindow4(self, MainWindow):
            self.process(r"D:\Howard_Feng\noteDetection\UserInterface\music_annotation_ui\guitar1.wav")
            self.currentWindow = QtWidgets.QMainWindow()
            self.win = Ui_SubWindow(self.currentWindow)
            self.win.setMusicId(4)
            self.currentWindow.show()

    def showSubWindow5(self, MainWindow):
            self.process(r"D:\Howard_Feng\noteDetection\UserInterface\music_annotation_ui\guitar2.wav")
            self.currentWindow = QtWidgets.QMainWindow()
            self.win = Ui_SubWindow(self.currentWindow)
            self.win.setMusicId(5)
            self.currentWindow.show()            
