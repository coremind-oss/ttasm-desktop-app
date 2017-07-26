from PyQt5 import QtCore
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QFormLayout, QHBoxLayout, QMessageBox
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QWidget
from http.cookies import SimpleCookie


#from utility import encrypt_data
class LoginForm(QWidget):

    def __init__(self, parent_tray):
        super(LoginForm, self).__init__()

        # keeping reference to parent
        self.parent_tray = parent_tray

        # define fixed size
        self.fixedWidth = 250
        self.fixedHeight = 100

        # no min, max, close button
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint)

        self.create_ui()
        self.move_to_primary_center()
        self.setWindowTitle("Log in")


    def create_ui(self):
        """Create user interface for login popup window"""

        emailLabel = QLabel("Email:")
        passwordLabel = QLabel("Password:")
        self.email = QLineEdit()
        self.password = QLineEdit()
        print (self.email.whatsThis())

        self.email.setPlaceholderText("Enter your email")
        self.password.setPlaceholderText("Enter your password")
        

        
        # Show asterisk in input instead of password chars
        self.password.setEchoMode(QLineEdit.Password)

        submitButton = QPushButton("Submit")

        # Usign lambda because Qt doesn't allow for arguments to by passed to slots
        # And we want to keep email and password as a private variables so we
        # don't want to make them direct members of Class and call them with self
        # directly inside self.submit() function
        submitButton.clicked.connect(lambda: self.submit(self.parent_tray,
                                                         self.email.text(),
                                                         self.password.text()))

        # Enter pressed inside password line edit
        self.password.returnPressed.connect(lambda: self.submit(self.parent_tray,
                                                           self.email.text(),
                                                           self.password.text()))
        
        self.email.returnPressed.connect(self.password.setFocus)
        
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.cancel)

        #Design a form layout
        formBox = QFormLayout()
        formBox.addRow(emailLabel, self.email)
        formBox.addRow(passwordLabel, self.password)
        
        # sign up label / link
        signUpLabel = QLabel()
        signUpLabel.setText('<a href="http://localhost:8000/sign-up/">Sign Up</a>')
        signUpLabel.setOpenExternalLinks(True)
        signUpLabel.show()
        
        # recover password link
        recoverLabel = QLabel()
        recoverLabel.setText('<a href="http://localhost:8000/recover-password/">Forgot your password?</a>')
        recoverLabel.setOpenExternalLinks(True)
        recoverLabel.show()
        
        # build sign up row
        signUpRow = QHBoxLayout()
        signUpRow.addWidget(signUpLabel)
        signUpRow.addWidget(recoverLabel)
        
        #add sign up row
        formBox.addRow(signUpRow)
        

        buttonRow = QHBoxLayout()
        buttonRow.addWidget(submitButton)
        buttonRow.addWidget(cancelButton)
        
        # add button row
        formBox.addRow(buttonRow)

        # Set layout for the Login Form (self)
        self.setLayout(formBox)

        try:
            last_user = open ('last_user', 'r').read()
            self.email.setText(last_user)
            self.password.setFocus()
        except:
            pass
        
        # Disable resize
        self.setFixedSize(self.fixedWidth, self.fixedHeight)

    def move_to_primary_center(self):
        """Reposition window to center of primary screen"""

        desktop = QDesktopWidget()
        primaryScreenIndex = desktop.primaryScreen()
        rectScreenPrimarty = desktop.screenGeometry(primaryScreenIndex)

        # center in the middle of screen, considering window's own size
        self.move(rectScreenPrimarty.center().x() - self.fixedWidth/2,
                  rectScreenPrimarty.center().y() - self.fixedHeight/2)


    def submit(self, parentTray, email, password):
        """Send data to server."""
        
        if not email or not password:
            
            msgBox = QMessageBox()
            info_text = []
            if not email:
                info_text.append('Email cannot be empty!')
            if not password:
                info_text.append('Password cannot be empty!')
            
            joined_info_text = '\n \n'.join(info_text)
            
            msgBox.setInformativeText(joined_info_text)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Oops!")

            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            msgBox.exec()

        else:
            url = parentTray.createURL('/accounts/login/')
            print('Trying to authenticate on', url)
            try:
                response = self.parent_tray.http_client.post(
                    url,
                    headers = {
                        'X-CSRFToken':self.parent_tray.http_client.cookies.get('csrftoken'),
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    data={
                        'login' : email,
                        'password' : password,
                        'client_public_key' : self.parent_tray.client_rsa.publickey().exportKey(),
                        'uuid' : parentTray.uuid
                    }
                )
                print(parentTray.uuid)
            except Exception as e:
                print ('No response, server may be down')
                
            cookie = SimpleCookie()
            cookie.load(response.request.headers['Cookie']) 
            if response.status_code == 200 and 'sessionid' in cookie:
                print("\nUser is logged in with session id: {}".format(cookie['sessionid'].value))
                parentTray.change_icon_on_login()
                parentTray.logged_in_state(True)
                parentTray.verify_initial_data()
                with open ('last_user' ,'w') as f:
                    f.write(email) 
                self.parent_tray.showMessage('Success',
                     'You are logged in as {}'.format(email),
                     parentTray.Information,
                     3000)
                self.close()
            else:
                msgBox = QMessageBox()
                msgBox.setInformativeText('Invalid email and/or password')
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowTitle("Oops!")
    
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                msgBox.exec()

    def cancel(self):
        """Close password input"""
        self.close()
