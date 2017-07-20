import json
import sys, os, requests, uuid
from threading import Thread
from time import sleep

from Crypto import Random
from Crypto.PublicKey import RSA
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QSystemTrayIcon

from login import LoginForm
from settings import HTTP_PROTOCOL
from settings import SERVER_URL
from timestamp.form import TimestampForm


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self):
        QSystemTrayIcon.__init__(self)

        self.setIcon(QIcon('icons/icon-placeholder_128x128_red.png'))
        
        self.http_client = requests.Session()
        self.base_url = '{}://{}'.format(HTTP_PROTOCOL, SERVER_URL)
        self.set_desktop_timezone()

        
        # Keeping reference to LoginForm object so that window wouldn't close
        
        
       
        
        self.uuid = self.create_uuid('TTASM')
        self.create_private_key()
        
        try:
            self.http_client.get(self.base_url)
            self.server_accessible = True
            self.set_server_public_key()
            self.present_login_form()
        except:
            self.server_accessible = False
            t = Thread(target=self.accessibility_worker)
            t.start()
        
        self.set_server_public_key()
        
        self.create_ui()
        
    def createURL(self, path):
        return '{}{}'.format(self.base_url, path)

    # Find Desktop's timezone   
    def set_desktop_timezone(self):
        response = requests.get('http://freegeoip.net/json')
        response_json = json.JSONDecoder().decode(response.text)
        self.timezone = response_json['time_zone']

    def verify_initial_data(self):
        url = self.createURL('/initial_synchronization/?timezone={}'.format(self.timezone))
        try:
            response = self.http_client.get(url)
            if response.status_code == 200:
                self.last_timestamp = response.text
            else:
                raise Exception('Server errror: {}'.format(response.status_code))
        except:
            print('Something is wrong with server comms')
    
    def set_server_public_key(self):
        #get server public key 

        url = self.createURL('/public_key/')
        print('Trying to get the public key from:', url) 
        
        try:
            response = self.http_client.get(url)
        except:
            print ('No response, server may be down')
            
        try:
            if response.status_code == 200:
                self.server_rsa_pub  = RSA.importKey(response.text)
                print ('Server private key aquired')
            else:
                print ('Server failed to provide public key')
        except:
            print("\nServer is not responding")
#             self.loginForm.close()
          
    def create_private_key(self):
        #Create new client RSA private key, public key and public key hash and store them to disk
        random_generator = Random.new().read
        self.client_rsa = RSA.generate(2048, random_generator)
        print ('Client private key created')

#         with open('./clientdata/client_RSA', 'wb') as f:
#             f.write(cl_rsa.exportKey())
#         with open('./clientdata/client_RSA.pub', 'wb') as f:
#             f.write(cl_rsa.publickey().exportKey())
#         with open('./clientdata/client_RSA.hash', 'w') as f:
#             f.write(SHA256.new(cl_rsa.publickey().exportKey()).hexdigest())
        
    print ('Client keys created')
    
    def create_ui(self):
        """Create user interface of Tray icon"""

        mainMenu = QMenu()
        subMenu = QMenu(mainMenu)
        subMenu.setTitle("Util")
        subButton_1 = subMenu.addAction("Show token")
        subButton_1.triggered.connect(self.show_token)
        subButton_2 = subMenu.addAction("Test sockets")
        subButton_2.triggered.connect(self.test_sockets)

        # Set the order of layout and add everything to main menu
        self.logInButton = mainMenu.addAction("Log in")
        self.logInButton.triggered.connect(self.present_login_form)
        
        self.simButton = mainMenu.addAction("Let's pretend server is accessible")
        self.simButton.triggered.connect(self.enable_login_etc)
        
        
        mainMenu.addSeparator()
        self.msgButton = mainMenu.addAction("Send message") # find a way how to hide this button to preserve action on it before user's log in action
        self.msgButton.triggered.connect(self.present_timestamp_form)
        
        if not self.server_accessible:
            self.logInButton.setEnabled(False)
            self.msgButton.setEnabled(False)
            
        
        mainMenu.addSeparator()
        mainMenu.addMenu(subMenu)
        mainMenu.addSeparator()
        exitButton = mainMenu.addAction("Exit")
        exitButton.triggered.connect(self.quit)

        self.setContextMenu(mainMenu)
    
    def accessibility_worker(self):
        while (not self.server_accessible):
            try:
                self.http_client.get(self.base_url)
                self.server_accessible = True
                self.enable_login_etc()
            except:
                sleep(5)

    def enable_login_etc(self):
        self.logInButton.setEnabled(True)
        self.msgButton.setEnabled(True)
    
    def create_uuid(self, UUID_string):
        return uuid.uuid3(uuid.NAMESPACE_DNS, UUID_string)

    def change_icon_on_login(self):
        self.setIcon(QIcon('icons/icon-placeholder_128x128_green.png'))
        
    def present_login_form(self):
        self.login_form = LoginForm(self)
        self.login_form.show()
    
    def present_timestamp_form(self):
        url = self.createURL('/last_activity_duration/')
        response = self.http_client.get(url)
        self.timestamp_form = TimestampForm(self, response.text)
        self.timestamp_form.show()

    def show_token(self):
        """Placeholder function"""
        
        try:
            self.showMessage('Token',
                             self.token,
                             QSystemTrayIcon.Information,
                             3000)
        except:
            self.showMessage('Token',
                             'No token received',
                             QSystemTrayIcon.Information,
                             3000)
    def test_sockets(self):
        """Placeholder function"""

        self.showMessage('Testing',
                         'Pending implementation',
                         QSystemTrayIcon.Information,
                         3000)


    def quit(self):
        """Exit program in a clean way."""
        if os.path.isfile('pid'):
            os.remove('pid') 
            print ("Deleting pid file")
        print ("Exiting")
        sys.exit(0)
        
