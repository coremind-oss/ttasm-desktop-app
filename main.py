import sys, os
from PyQt5.QtWidgets import QApplication
from tray import SystemTrayIcon

def alreadyRunnig(name):
    os.system('ps -ef > /tmp/ttasm')
    lines=open('/tmp/ttasm', 'r').read().split('\n')
    count=0
    for line in lines:
        if name in line:
            count+=1
    print ('Found {} mentions of ttasm in ps'.format(count))
    if (count>1):
        return True
    else:
        return False

def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    
    systemTrayIcon = SystemTrayIcon()
    systemTrayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__': 
    
    pid = str(os.getpid())
    print (pid)
    if (alreadyRunnig("ttasm-desktop-app")):
        print ('Ttasm already running, exiting...')
    else:
        main()