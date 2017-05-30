from PyQt5.QtWidgets import QFormLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5 import QtCore


class LoginForm(QWidget):

    def __init__(self):
        super(LoginForm, self).__init__()

        # define fixed size
        self.fixedWidth = 250
        self.fixedHeight = 100

        # no min, max, close button
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint)

        self.create_ui()
        self.move_to_primary_center()


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

        pushBoxLayout = QHBoxLayout()
        pushBoxLayout.addWidget(submitButton)
        pushBoxLayout.addWidget(cancelButton)

        formBox.addRow(pushBoxLayout)

        # Set layout for the Login Form (self)
        self.setLayout(formBox)

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


    def submit(self):
        """Send data to server."""
        pass


    def cancel(self):
        """Close password input"""
        self.close()
