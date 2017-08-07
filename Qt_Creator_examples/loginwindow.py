# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.Qt import QCursor


class Ui_LoginWindow(object):
    
    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())

    def mouseReleaseEvent(self, QMouseEvent):
        cursor =QtGui.QCursor()
        print(cursor.pos())

    def setupUi(self, LoginWindow):
        
        
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(422, 271)
        LoginWindow.setStyleSheet("#LoginWindow{\n"
"background-color: rgb(179, 246, 179);\n"
"}")    
        LoginWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.centralWidget = QtWidgets.QWidget(LoginWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.email = QtWidgets.QLabel(self.layoutWidget)
        self.email.setStyleSheet("#email{\n"
"font-family: \"Monospace\";\n"
"font-weight:bold;\n"
"color:rgb(0, 191, 25);\n"
"}")
        self.email.setObjectName("email")
        self.horizontalLayout_4.addWidget(self.email)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.password = QtWidgets.QLabel(self.layoutWidget)
        self.password.setStyleSheet("#password{\n"
"font-family: \"Monospace\";\n"
"font-weight:bold;\n"
"color:rgb(0, 191, 25);\n"
"}")
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 120, 401, 139))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.submit = QtWidgets.QPushButton(self.layoutWidget1)
        self.submit.setStyleSheet("#submit {\n"
"    background-color:rgb(0, 191, 25);\n"
"    border-bottom-right-radius:30px;\n"
"    border-top-left-radius:30px;\n"
"    border:3px solid white;\n"
"    color:white;\n"
"    font-family:Monospace;\n"
"    font-size:17px;\n"
"    font-weight:bold;\n"
"    padding:12px 44px;\n"
"    text-decoration:none;\n"
"    width:60px;\n"
"    height:20px;\n"
"    }\n"
"#submit:hover {\n"
"    background-color:white;\n"
"    border-color:rgb(0, 191, 25);\n"
"    color:rgb(0, 191, 25);\n"
"}\n"
"#submit:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}")
        self.submit.setObjectName("submit")
        self.horizontalLayout_2.addWidget(self.submit)
        self.cancel = QtWidgets.QPushButton(self.layoutWidget1)
        self.cancel.setEnabled(True)
        self.cancel.setStyleSheet("#cancel {\n"
"    background-color:rgb(0, 191, 25);\n"
"    border-bottom-right-radius:30px;\n"
"    border-top-left-radius:30px;\n"
"    border:3px solid white;\n"
"    color:white;\n"
"    font-family:Monospace;\n"
"    font-size:17px;\n"
"    font-weight:bold;\n"
"    padding:12px 44px;\n"
"    text-decoration:none;\n"
"    width:60px;\n"
"    height:20px;\n"
"    }\n"
"#cancel:hover {\n"
"    background-color:white;\n"
"    border-color:rgb(0, 191, 25);\n"
"    color:rgb(0, 191, 25);\n"
"}\n"
"#cancel:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        LoginWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(LoginWindow)
        self.statusBar.setObjectName("statusBar")
        LoginWindow.setStatusBar(self.statusBar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.email.setText(_translate("LoginWindow", "Email:"))
        self.password.setText(_translate("LoginWindow", "Password:"))
        self.submit.setText(_translate("LoginWindow", "Submit"))
        self.cancel.setText(_translate("LoginWindow", "Cancel"))



class CustomWindow(QtWidgets.QMainWindow):

    lastX = None
    lastY = None
    draggable = False
    
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
    
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

