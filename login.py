from PyQt5.QtWidgets import QFormLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5 import QtCore


class LoginForm(QWidget):

    def __init__(self, parentTray):
        super(LoginForm, self).__init__()

        # keeping reference to parent
        self.parentTray = parentTray

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

        # Usign lambda because Qt doesn't allow for arguments to by passed to slots
        # And we want to keep username and password as a private variables so we
        # don't want to make them direct members of Class and call them with self
        # directly inside self.submit() function
        submitButton.clicked.connect(lambda: self.submit(self.parentTray,
                                                         username.text(),
                                                         password.text()))

        # Enter pressed inside password line edit
        password.returnPressed.connect(lambda: self.submit(self.parentTray,
                                                           username.text(),
                                                           password.text()))

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


    def submit(self, parentTray, username, password):
        """Send data to server."""

        parentTray.showMessage("Can't do that yet",
                               "Sorry {}, but login ins't implemented yet :(".format(username),
                               QSystemTrayIcon.Critical,
                               8000)

        self.close()


    def cancel(self):
        """Close password input"""
        self.close()
