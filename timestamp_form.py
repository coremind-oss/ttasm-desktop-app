from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QFormLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QTextEdit, QMessageBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


from datetime import datetime
import json
import pytz
import requests


class TimestampForm(QWidget):
    
    def __init__(self,parentTray):
        super(TimestampForm,self).__init__()
        
        self.parentTray = parentTray
        
        self.height = 400
        self.width =  150
        
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint)
        
        self.setWindowTitle('Message')
        
        self.create_ui()
        
        
    def create_ui(self):
        
        msgLabel = QLabel('What were you doing in the period?')
        self.message = QLineEdit()
        
        self.message.setPlaceholderText('Enter text here...')
        
        sendButton = QPushButton('Send')
        cancelButton = QPushButton('Cancel')
        
        cancelButton.clicked.connect(self.cancel)
        sendButton.clicked.connect(lambda: self.send_timestamp(self.message.text()))
        formBox = QFormLayout()
        formBox.addRow(msgLabel)
        formBox.addRow(self.message)
        
        buttonRow = QHBoxLayout()
        buttonRow.addWidget(sendButton)
        buttonRow.addWidget(cancelButton)
        
        formBox.addRow(buttonRow)
        
        self.setLayout(formBox)
        
        self.setFixedSize(self.height, self.width)
        
#         just for checking

    def send_timestamp(self, message):

        if not message:
     
            msgBox = QMessageBox()
            text_info = [] 
     
            if not message:
     
                text_info.append('You have not send any message')
                error_info_text = ''.join(text_info)
                  
                msgBox.setInformativeText(error_info_text)
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowTitle('Error')
                msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                msgBox.addButton(QMessageBox.Ok)
                msgBox.exec()
     
        else:
            self.desktop_timezone() 
            print('\nSent message is{}'.format(message)) 

#             url = '{}://{}/timestamp_message_handling/{}'.format('http','127.0.0.1:8000',message)
            
#             print(url)
        
#     Finding a desktop IP and from that find a Desktop's timezone   
    def desktop_timezone(self):
     
    # getting desktop IP address with ipify api
         
        my_ip = "https://api.ipify.org"
        response_ip = requests.get(my_ip)
        print("User's IP is {}".format(response_ip.text))
         
    # getting json object including timezone for current desktop with ip-api
         
        url = "http://ip-api.com/json/{}".format(response_ip.text)
        response = requests.get(url)
        print("\nReceived JSON object : {} ".format(response.text))
        response_text = response.text
        response_json = json.JSONDecoder().decode(response_text)
    #     print(type(response_json))
        current_timezone = response_json['timezone']
        print("\nUser's timezone is: {}".format(current_timezone))
    
    # Provide a local time according to timezone
         
        desktop_loc_time = pytz.timezone(current_timezone)
        fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        
        loc_dt = desktop_loc_time.localize(datetime.now())
        print ("\nLocal time for desktop location is: {}".format(loc_dt.strftime(fmt)))


        
         
    
        
    def cancel(self):
        self.hide()
