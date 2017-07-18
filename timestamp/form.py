from PyQt5 import QtCore
from PyQt5.Qt import QFormLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QMessageBox, QSystemTrayIcon
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
import pytz

from timestamp.utils import human_time


class TimestampForm(QWidget):
    
    def __init__(self, parentTray):
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
        
        msgLabel = QLabel('What were you doing for the past')
#         msgLabel = QLabel('What were you doing for the past {}?'.format(self.calc_time_spent()))
        self.message = QLineEdit()
        
        self.message.setPlaceholderText('Enter text here...')
        
        sendButton = QPushButton('Send (enter)')
        cancelButton = QPushButton('Cancel (escape)')
        
        
        cancelButton.clicked.connect(self.cancel)
        
        
        sendButton.clicked.connect(lambda: self.send_timestamp(self.parentTray, self.message.text()))
        self.message.returnPressed.connect(lambda: self.send_timestamp(self.parentTray, self.message.text()))
        
        formBox = QFormLayout()
        formBox.addRow(msgLabel)
        formBox.addRow(self.message)
        
        buttonRow = QHBoxLayout()
        buttonRow.addWidget(sendButton)
        buttonRow.addWidget(cancelButton)
        
        formBox.addRow(buttonRow)
        
        self.setLayout(formBox)
        
        self.setFixedSize(self.height, self.width)

    def calc_time_spent(self):
        if not hasattr(self.parentTray, 'last_timestamp'):
            print('get server time attempt')
            url = self.parentTray.createURL('/get_last_timestamp/')
            response = self.parentTray.http_client(url)

#    TODO: this needs to be parsed from the timestamp format used on the server
# it will also be in UTC and needs to be converted into the desktop's timezone
#             previousTime = datetime.strptime(response.text, '%Y-%m-%d').astimezone(tzinfo-object)
            print(response)
        
        else:
            previousTime = self.parentTray.last_timestamp
        currentTime = pytz.timezone(self.parentTray.timezone)
        time_spent = currentTime - previousTime
        return human_time(time_spent)

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

            url = self.parentTray.createURL('/timestamp_message_handling/')
             
            print("Trying to send data to {}".format(url))

            try:
                response = self.parentTray.http_client.post(
                    url,
                    headers = {
                        'X-CSRFToken': self.parentTray.http_client.cookies.get('csrftoken'),
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    data={
                        'message': message,
                        'timezone': self.parentTray.timezone,
                    }
                )

            except Exception as e:
                response = DummyResponse(-1, 'ConnectionError')
            print(response.text)
#             print('THIS IS RESPONSE\n\n{}'.format(response.text))

            
            if response.status_code == 200:
                
                self.parentTray.showMessage(
                    'Your message is: ',
                    message ,
                    QSystemTrayIcon.Information,
                    3000,
                )
                
                self.close()
                
                self.message.setText('')
            else:
                self.close()
                self.parentTray.showMessage(
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