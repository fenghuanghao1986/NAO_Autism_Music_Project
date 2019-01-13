#Digital Image Process
#main.py
from PyQt5 import QtGui, QtWidgets
from DIP import *
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    win = Ui_MainWindow(window)
    window.show()
    sys.exit(app.exec_())
main()
