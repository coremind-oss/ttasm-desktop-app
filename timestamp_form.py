from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QFormLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QTextEdit
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


class TimestampForm(QWidget):
    
    def __init__(self,parentTray):
        super(TimestampForm,self).__init__()
        
        self.parentTray = parentTray
        
        self.height = 400
        self.width =  150
        
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint)
        
        self.create_ui()
#         self.center_position()
        
    def create_ui(self):
        
        msgLabel = QLabel('What are you working on ?')
        self.message = QTextEdit()
        
        self.message.setPlaceholderText('Enter text here...')
        
        sendButton = QPushButton('Send !')
        cancelButton = QPushButton('Cancel')
        
        cancelButton.clicked.connect(self.cancel)
        
        formBox = QFormLayout()
        formBox.addRow(msgLabel)
        formBox.addRow(self.message)
        
        buttonRow = QHBoxLayout()
        buttonRow.addWidget(sendButton)
        buttonRow.addWidget(cancelButton)
        
        formBox.addRow(buttonRow)
        
        self.setLayout(formBox)
        
        self.setFixedSize(self.height, self.width)
        
        
    def cancel(self):
        self.close()
        print('Message box closed')