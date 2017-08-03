# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(567, 368)
        LoginWindow.setStyleSheet("#LoginWindow{\n"
"background-color: rgb(179, 246, 179);\n"
"}")
        self.centralWidget = QtWidgets.QWidget(LoginWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(30, 27, 336, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.email = QtWidgets.QLabel(self.widget)
        self.email.setStyleSheet("#email{\n"
"font-family: \"Monospace\";\n"
"font-weight:bold;\n"
"color:rgb(0, 191, 25);\n"
"}")
        self.email.setObjectName("email")
        self.horizontalLayout_4.addWidget(self.email)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.password = QtWidgets.QLabel(self.widget)
        self.password.setStyleSheet("#password{\n"
"font-family: \"Monospace\";\n"
"font-weight:bold;\n"
"color:rgb(0, 191, 25);\n"
"}")
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.widget1 = QtWidgets.QWidget(self.centralWidget)
        self.widget1.setGeometry(QtCore.QRect(30, 150, 401, 139))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.submit = QtWidgets.QPushButton(self.widget1)
        self.submit.setStyleSheet("#submit {\n"
"    background-color:rgb(0, 191, 25);\n"
"    border-radius:5px;\n"
"    border:3px solid white;\n"
"    color:white;\n"
"    font-family:Monospace;\n"
"    font-size:17px;\n"
"    font-weight:bold;\n"
"    padding:12px 44px;\n"
"    text-decoration:none;\n"
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.cancel = QtWidgets.QPushButton(self.widget1)
        self.cancel.setEnabled(True)
        self.cancel.setStyleSheet("#cancel {\n"
"    background-color:rgb(0, 191, 25);\n"
"    border-radius:5px;\n"
"    border:3px solid white;\n"
"    color:white;\n"
"    font-family:Monospace;\n"
"    font-size:17px;\n"
"    font-weight:bold;\n"
"    padding:12px 44px;\n"
"    text-decoration:none;\n"
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.password.raise_()
        self.lineEdit.raise_()
        self.email.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        LoginWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(LoginWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 567, 22))
        self.menuBar.setObjectName("menuBar")
        LoginWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(LoginWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        LoginWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

