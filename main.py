import sys
from PyQt5.QtWidgets import QApplication
from tray import SystemTrayIcon


def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    
    systemTrayIcon = SystemTrayIcon()
    systemTrayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__': main()
