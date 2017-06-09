import sys, os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QSystemTrayIcon

from login import LoginForm


class SystemTrayIcon(QSystemTrayIcon):


    def __init__(self):
        icon = QIcon('icons/icon-placeholder_128x128.png')
        super(SystemTrayIcon, self).__init__(icon)

        self.create_ui()


    def create_ui(self):
        """Create user interface of Tray icon"""

        mainMenu = QMenu()

        subMenu = QMenu(mainMenu)
        subMenu.setTitle("Submenu")
        subButton_1 = subMenu.addAction("Action 1")
        subButton_1.triggered.connect(self.action_1)
        subButton_2 = subMenu.addAction("Action 2")
        subButton_2.triggered.connect(self.action_2)

        # Set the order of layout and add everything to main menu
        logInButton = mainMenu.addAction("Log in")
        logInButton.triggered.connect(self.login)
        mainMenu.addSeparator()
        mainMenu.addMenu(subMenu)
        mainMenu.addSeparator()
        exitButton = mainMenu.addAction("Exit")
        exitButton.triggered.connect(self.quit)

        self.setContextMenu(mainMenu)


    def login(self):
        """Authenticate via webserver."""

        # Keeping reference to LoginForm object so that window wouldn't close
        self.loginForm = LoginForm(parentTray = self)
        self.loginForm.show()


    def action_1(self):
        """Placeholder function"""

        self.showMessage('Action 1',
                         'You triggered action 1',
                         QSystemTrayIcon.Information,
                         3000)


    def action_2(self):
        """Placeholder function"""

        self.showMessage('Action 2',
                         'You triggered action 2',
                         QSystemTrayIcon.Information,
                         3000)


    def quit(self):
        """Exit program in a clean way."""
        if os.path.isfile('pid'):
            os.remove('pid') 
            print ("Deleting pid file")
        print ("Exiting")
        sys.exit(0)
