import sys
from time import sleep

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QSystemTrayIcon


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self):
        QSystemTrayIcon.__init__(self, QIcon('icons/icon-placeholder_128x128.png'))
        
        # Initialize menu
        mainMenu = QMenu()
        mainMenu.setTitle("Main Menu")
        
        # Create submenus and populate them with items
        subMenu1 = QMenu(mainMenu)
        subMenu1.setTitle('Submenu1') # Not sure what this does
        subMenu1ButtonA=subMenu1.addAction("Action A")
        subMenu1ButtonA.triggered.connect(self.subMenu1ButtonAAction)
        subMenu1.addAction("Action B")
        subMenu1.addAction("Action B")

        subMenu2 = QMenu(mainMenu)
        subMenu2.setTitle('Submenu2')
        subMenu2.addAction("Action D")
        subMenu2.addAction("Action E")
        subMenu2.addAction("Action F")      
          
        # Populate Main Menu
        mainMenu.addMenu(subMenu1)
        menu1Button = mainMenu.addAction("Menu1")
        menu1Button.triggered.connect(self.menu1Action)
       
        mainMenu.addMenu(subMenu2)
        
        exitButton = mainMenu.addAction("Exit")
        exitButton.triggered.connect(self.quit)
 
 
                 
        # Set the menu as context menu
        self.setContextMenu(mainMenu)
   
    def menu1Action(self):
        print ("MainMenu button2 stuff")
        
    def subMenu1ButtonAAction(self):
        print ("Submenu1 First button stuff")
        
    def quit(self):
#         self.showMessage(
#         'title {}'.format(1),
#         'Quitting in {} seconds'.format(1),
#         QSystemTrayIcon.Warning,
#         500)
#         sleep(1)
        print ('Clean exit')
        sys.exit(0)