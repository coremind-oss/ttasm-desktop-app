from datetime import datetime
import json

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QFormLayout, QHBoxLayout, QKeySequence
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QTextEdit, QMessageBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
import pytz
import requests


class TimestampForm(QWidget):
    
    def __init__(self,parentTray):
        super(TimestampForm,self).__init__()
        
        self.parentTray = parentTray
        
        self.height = 300
        self.width =  100
        
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint)
     
        
        self.setWindowTitle('Message')
        
        self.create_ui()
        
        
        
    def create_ui(self):
        
        msgLabel = QLabel('What were you doing in the period < time2 - time1 >?')
        self.message = QLineEdit()
        
        self.message.setPlaceholderText('Enter text here...')
        
        sendButton = QPushButton('Send (enter)')
        cancelButton = QPushButton('Cancel (escape)')
        
        
        cancelButton.clicked.connect(self.cancel)
        
        
        sendButton.clicked.connect(lambda: self.send_timestamp(self.message.text()))
        self.message.returnPressed.connect(lambda: self.send_timestamp(self.message.text()))
        
        formBox = QFormLayout()
        formBox.addRow(msgLabel)
        formBox.addRow(self.message)
        
        buttonRow = QHBoxLayout()
        buttonRow.addWidget(sendButton)
        buttonRow.addWidget(cancelButton)
        
        formBox.addRow(buttonRow)
        
        self.setLayout(formBox)
        
        self.setFixedSize(self.height, self.width)
        
#     find a Desktop's timezone   
    def desktop_timezone(self):
        url = "http://freegeoip.net/json"
        response = requests.get(url)
        print("\nReceived JSON object : {} ".format(response.text))
        response_json = json.JSONDecoder().decode(response.text)
        print("\nUser's timezone is: {}".format(response_json['time_zone']))
        
    # Provide a local time according to timezone
         
        desktop_loc_time = pytz.timezone(response_json['time_zone'])
        fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        
        self.loc_dt = desktop_loc_time.localize(datetime.now())
        
        self.formated_time = self.loc_dt.strftime(fmt)
        
        return self.formated_time
        
#         print ("\nLocal time for desktop location is: {}".format(self.formated_time))

        

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
            
            print('\nThis is the local time of the user: {} '.format(self.formated_time))

            print('\nSent message is: {}'.format(message))

            

            url = '{}://{}/timestamp_message_handling/'.format('HTTP','127.0.0.1:8000')
             
            print("Trying to send data to {}".format(url))
            

            client = requests.session()
            client.get(url)
            try:
                response = client.post(
                    url,
                    headers = {
                        'X-CSRFToken':client.cookies.get('csrftoken'),
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    data={
                        'message': message,
                        'timestamp': self.formated_time
                    }
                )
                 
             
            except Exception as e:
                print('there is no proper server')
            print(response.text)
#             print('THIS IS RESPONSE\n\n{}'.format(response.text))

            
            if response.text == 'Server receive message':
                msgBox = QMessageBox()
                msgBox.setInformativeText('Server receive message \n-> {} <- \npending writing into databaze'.format(message))
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowTitle("Message")
     
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                msgBox.exec()
                self.close() 
                

    def keyPressEvent(self, event):
        
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        

    def cancel(self):
        self.message.setPlaceholderText('Enter text here...')
        self.hide()
    