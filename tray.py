from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self):
        QSystemTrayIcon.__init__(self, QIcon('icons/icon-placeholder_128x128.png'))