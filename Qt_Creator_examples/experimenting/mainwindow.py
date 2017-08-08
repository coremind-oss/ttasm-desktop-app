# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QCursor
from PyQt5.QtWidgets import QDesktopWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1199, 675)
        MainWindow.setStyleSheet("background-image: url(images/Untitled-3.png);")
        
        self.move_to_primary_center(MainWindow)
        
    def move_to_primary_center(self, window):
        desktop = QDesktopWidget()
        primaryScreenIndex = desktop.primaryScreen()
        rectScreenPrimary = desktop.screenGeometry(primaryScreenIndex)
        
        geometry = window.geometry()
        window.move(rectScreenPrimary.center().x() - geometry.width()/2,
                  rectScreenPrimary.center().y() - geometry.height()/2)

class CustomWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(CustomWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.lastX = None
        self.lastY = None
        self.draggable = False
    
    def keyPressEvent(self, e):
        print(e)
        
    def mousePressEvent(self, e):
        self.draggable = True
    
    def mouseMoveEvent(self, e):
        if self.draggable:
            if not self.lastX: self.lastX = e.x()
            if not self.lastY: self.lastY = e.y()
            
            p = QCursor.pos()
            g = self.geometry()
            g.moveTo(p.x()-self.lastX, p.y()-self.lastY)
            self.setGeometry(g)
    
    def mouseReleaseEvent(self, e):
        if self.lastX: self.lastX = None
        if self.lastY: self.lastY = None
        self.draggable = False
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = CustomWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())