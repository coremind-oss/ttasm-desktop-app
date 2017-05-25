import sys
from time import sleep

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QSystemTrayIcon


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self):
        QSystemTrayIcon.__init__(self, QIcon('icons/icon-placeholder_128x128.png'))
        
        # Initialize menu
        menu = QMenu()
        exitButton = menu.addAction("Exit")
        exitButton.triggered.connect(self.quit)
                
        # Set the menu as context menu
        self.setContextMenu(menu)
        
    def quit(self):
        for i in range(5):
            self.showMessage(
                'title {}'.format(i + 1),
                'Quitting in {} seconds'.format(i + 1),
                QSystemTrayIcon.Warning,
                500,
            )
            sleep(1)
        sys.exit(0)