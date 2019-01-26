# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 23:50:43 2019

@author: CV_LAB_Howard
"""

from PyQt5 import QtGui, QtWidgets
from mainwindow import *
import sys

def main():
    
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
        
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    win = Ui_MainWindow(window)
    window.show()
    sys.exit(app.exec_())

main()