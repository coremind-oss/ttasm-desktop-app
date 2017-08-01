from PyQt5 import QtCore
from PyQt5.Qt import QFormLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QMessageBox, QSystemTrayIcon
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget



class TimestampForm(QWidget):
    
    def __init__(self, parent_tray, time_passed):
        super(TimestampForm, self).__init__()
        
        self.parent_tray = parent_tray
        self.time_passed = time_passed
        
        self.height = 300
        self.width =  100
        
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint)
     
        
        self.setWindowTitle('Message')
        
        self.create_ui()
        
        
        
        
        
    def create_ui(self):
        print(type(self.time_passed))
        msgLabel = QLabel('What were you doing for the past {}?'.format(self.time_passed))
        self.message = QLineEdit()
        
        self.message.setPlaceholderText('Enter text here...')
        
        sendButton = QPushButton('Send (enter)')
        cancelButton = QPushButton('Cancel (escape)')
        
        
        cancelButton.clicked.connect(self.cancel)
        
        
        sendButton.clicked.connect(lambda: self.send_timestamp(self.parent_tray, self.message.text()))
        self.message.returnPressed.connect(lambda: self.send_timestamp(self.parent_tray, self.message.text()))
        
        formBox = QFormLayout()
        formBox.addRow(msgLabel)
        formBox.addRow(self.message)
        
        buttonRow = QHBoxLayout()
        buttonRow.addWidget(sendButton)
        buttonRow.addWidget(cancelButton)
        
        formBox.addRow(buttonRow)
        
        self.setLayout(formBox)
        
        self.setFixedSize(self.height, self.width)

    def send_timestamp(self, parentTray, message):
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
            print('\nSent message is: {}'.format(message))

            url = self.parent_tray.createURL('/timestamp_message_handling/')
             
            print("Trying to send data to {}".format(url))

            try:
                response = self.parent_tray.http_client.post(
                    url,
                    headers = {
                        'X-CSRFToken': self.parent_tray.http_client.cookies.get('csrftoken'),
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    data={
                        'message': message,
                        'timezone': self.parent_tray.timezone,
                    }
                )

            except Exception as e:
                response = DummyResponse(-1, 'ConnectionError')
            print(response.text)
#             print('THIS IS RESPONSE\n\n{}'.format(response.text))

            
            if response.status_code == 200:
                
                self.parent_tray.showMessage(
                    'Your message is: ',
                    message ,
                    QSystemTrayIcon.Information,
                    3000,
                )
                
                self.close()
                
                self.message.setText('')
            else:
                self.close()
                self.parent_tray.showMessage(
                    'Error: ',
                    'Your message wasn\'t sent.\nReason: {}'.format(response.text),
                    QSystemTrayIcon.Critical,
                    5000,
                )
                

    def keyPressEvent(self, event):
        
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def cancel(self):
        self.message.setPlaceholderText('Enter text here...')
        self.hide()

class DummyResponse():
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text