import json
import sys, os, requests, uuid

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
#         icon = QIcon('icons/icon-placeholder_128x128_red.png')
#         super(SystemTrayIcon, self).__init__(icon)
        
        self.http_client = requests.Session()
        self.base_url = '{}://{}'.format(HTTP_PROTOCOL, SERVER_URL)

        self.set_desktop_timezone()
        self.verify_base_date()
        self.set_server_public_key()
        self.uuid = self.create_uuid('TTASM')
        print('UUID {} created'.format(self.uuid))
        self.create_private_key()
        self.create_ui()
        # Keeping reference to LoginForm object so that window wouldn't close
        self.loginForm = LoginForm(parentTray = self)
        self.timestamp_form = TimestampForm(parentTray = self)
        self.show_login()
        
    def getURL(self, path):
        return '{}{}'.format(self.base_url, path)

    # Find Desktop's timezone   
    def set_desktop_timezone(self):
        response = requests.get('http://freegeoip.net/json')
        response_json = json.JSONDecoder().decode(response.text)
        self.timezone = response_json['time_zone']

    def verify_base_date(self):
        url = self.getURL('/init_base_date/')
        try:
            response = self.http_client.get(url)
            if response.status_code != 200:
                raise Exception('Base date not set properly')
            else:
                print('DailyActivity object base_date verified')
        except:
            print ('No response, server may be down')

    def set_server_public_key(self):
        #get server private key 

        url = self.getURL('/public_key/')
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
            self.quit()

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
        logInButton = mainMenu.addAction("Log in")
        logInButton.triggered.connect(self.show_login)
        
        mainMenu.addSeparator()
        msgButton = mainMenu.addAction("Send message") # find a way how to hide this button to preserve action on it before user's log in action
        msgButton.triggered.connect(self.show_timestamp_form)
        
        
        mainMenu.addSeparator()
        mainMenu.addMenu(subMenu)
        mainMenu.addSeparator()
        exitButton = mainMenu.addAction("Exit")
        exitButton.triggered.connect(self.quit)

        self.setContextMenu(mainMenu)
    
    def create_uuid(self, UUID_string):
        return uuid.uuid3(uuid.NAMESPACE_DNS, UUID_string)

    def change_icon_on_login(self):
        self.setIcon(QIcon('icons/icon-placeholder_128x128_green.png'))

    def show_login(self):
        self.loginForm.show()

    def show_timestamp_form(self):
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
