import sys, os
from PyQt5.QtWidgets import QApplication
from tray import SystemTrayIcon
import psutil


def spawnPIDfile(currentProc):
    with open('pid', 'w') as pidFile:
        pidFile.write(str(currentProc.pid))
        pidFile.close()
    return False

def alreadyRunnigPU():
    
    # Check if pid file exists. If not, create one, write down current pid and return False (another instance not running so loading can resume). 
    # If pid file exists, read pid from it. If that process is running, return True (program already trunning, so main() doesn't start).
    # Otherwise delete pid file, create new one with updated pid entry and return False (old process is dead, so loading can resume).
    
    currentProc = psutil.Process()
    print ('PsUtil info:')
    print ('ProcName:', currentProc.name(), 'id:', currentProc.pid, 'status:', currentProc.status())
    print ('Proc children:', currentProc.children())
    print ('ProcParent:', currentProc.parent(),)
    print('Full path:', psutil.Process().exe())
    print('Current working directory:', currentProc.cwd())
     
    if not os.path.exists('./pid'):
        print ('Pid file not found, creating pid file & loading')
        return spawnPIDfile(currentProc)
        
    else:
        with open('pid', 'r') as f: 
            pid = int(f.read())
        print ('\nPid file found, last entry is:', pid)

        if psutil.pid_exists(pid):
            if 'python' in psutil.Process(pid).name():
                print ('Program instance with pid {} already running\nExiting...'.format(pid))
                return True
        else:
            print ('Found earlier instance with pid {} but it\'s not running'.format(pid))
            if os.path.isfile('pid'):
                os.remove('pid') 
            return spawnPIDfile(currentProc)


def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    
    systemTrayIcon = SystemTrayIcon()
    systemTrayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if alreadyRunnigPU():
        print ('Goodbye')
    else:
        print ('Loading')
        main()
