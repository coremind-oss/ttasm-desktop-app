import sys, subprocess
from PyQt5.QtWidgets import QApplication
from tray import SystemTrayIcon


def alreadyRunnig(searchString):
    #capture stdout of 'ps -ef' and return false if number of ttasm-desktop-app processes is > 1
    print ('Checking for multiple instances...')
    result= subprocess.Popen(["ps", "-ef"], stdout=subprocess.PIPE)
    (out, err) = result.communicate()
    lines=str(out.decode()).split('\n')
    count=0
    for line in lines:
        if searchString in line:
            count+=1
    print ('Found {} mentions of ttasm in ps -ef'.format(count))
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
 
    if (alreadyRunnig("ttasm-desktop-app")):
        print ('TTASM already running, exiting...')
    else:
        print ('Loading')
        main()