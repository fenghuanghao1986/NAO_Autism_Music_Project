# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:03:05 2019

@author: CV_LAB_Howard
"""

import sys
from PyQt4 import QtCore, QtGui, uic

#from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

qtCreatorFile = "interface_test_1.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
