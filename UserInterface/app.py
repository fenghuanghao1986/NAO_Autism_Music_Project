# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:02:02 2019

@author: CV_LAB_Howard
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from interface import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
#        super(App).__init__()
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        
app = QApplication(sys.argv)
w = Ui_MainWindow()
w.setupUi(QMainWindow)
sys.exit(app.exec_())