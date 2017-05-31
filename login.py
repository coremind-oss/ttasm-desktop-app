from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5 import QtCore


class LoginForm(QWidget):

    def __init__(self):
        super(LoginForm, self).__init__()

        # Specify window properties of the window, we want it to behave like popup
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint  | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowTitleHint)


        self.create_ui()
        self.moveToCenter()
        

    def moveToCenter(self):
        
        # get widget size
        loginSize=self.frameSize()
        
        # get center point of primary monitor
        desktop = QDesktopWidget()
        print ('Number of screens is', desktop.screenCount())
        print ('Primary screen is', desktop.primaryScreen())

        desktopRect=desktop.screenGeometry(desktop.primaryScreen())
        centerPoint=desktopRect.center()
        print (desktopRect)
        print ('\n')
        print (centerPoint.x(), centerPoint.y(), type (centerPoint))
        
        # move widget to center of primary monitor
        self.move(centerPoint.x()-loginSize.width() * .5, centerPoint.y()-loginSize.height() * .5)


    def create_ui(self):
        """Create user interface for login popup window"""

        usernameLabel = QLabel("Username:")
        passwordLabel = QLabel("Password:")
        username = QLineEdit()
        password = QLineEdit()

        # Show asterisk in input instead of password chars
        password.setEchoMode(QLineEdit.Password)

        submitButton = QPushButton("Submit")
        submitButton.clicked.connect(self.submit)
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.cancel)

        #Design a form layout
        formBox = QFormLayout()
        formBox.addRow(usernameLabel, username)
        formBox.addRow(passwordLabel, password)
        formBox.addRow(submitButton, cancelButton)

        # Set layout for the Login Form (self)
        self.setLayout(formBox)

        self.setFixedSize(250,110)


    def to_top_right(self):
        """Reposition popup to the top right corner"""

        desktop = QDesktopWidget()
        dx = desktop.availableGeometry().width()
        dy = desktop.availableGeometry().height()

        wh = 70 #height
        ww = 250 #width

        self.setGeometry(dx-ww, 40, ww, wh)

    def submit(self):
        """Send data to server."""
        pass


    def cancel(self):
        """Close password input"""
        self.close()
