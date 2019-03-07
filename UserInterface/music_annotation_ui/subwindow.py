# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Emotion_selections_subwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SubWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.musicId = -1
        self.choice = -1
        self.setupUi(parent)
        #self.radioButton.clicked.connect(self.save)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.save)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(245, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 161, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.radioButton_5 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_5)
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.radioButton_4)
        self.radioButton_6 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.radioButton_6)
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(40, 210, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 245, 21))
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
        self.radioButton_5.setText(_translate("MainWindow", "Happy"))
        self.radioButton.setText(_translate("MainWindow", "Sad"))
        self.radioButton_3.setText(_translate("MainWindow", "Angry"))
        self.radioButton_4.setText(_translate("MainWindow", "Peaceful"))
        self.radioButton_6.setText(_translate("MainWindow", "Chill"))
        self.radioButton_2.setText(_translate("MainWindow", "None"))
        
    def setMusicId(self, id):
        self.musicId = id

    def save(self, MainWindow):
        if (self.radioButton.isChecked()):
            self.choice = 0
        elif (self.radioButton_2.isChecked()):
            self.choice = 1
        elif (self.radioButton_3.isChecked()):
            self.choice = 2
        elif (self.radioButton_4.isChecked()):
            self.choice = 3
        elif (self.radioButton_5.isChecked()):
            self.choice = 4
        elif (self.radioButton_6.isChecked()):
            self.choice = 5
            
        file = open("data.txt", "a")
        file.write(str(self.musicId)+str(self.choice))
        file.close()
