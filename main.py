import sys, os
from PyQt5.QtWidgets import QApplication
from tray import SystemTrayIcon
from psutil import Process, pid_exists


def alreadyRunnig(searchString):
    #capture stdout of 'ps -ef' and return true if number of ttasm-desktop-app processes is > 1
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

def alreadyRunnigPU(inputStr):
    
    #Check if pid file exists. If not, create one, write down current pid and return False (another instance not running so loading can resume). 
    #If pid file exists, read pid from it. If that process is running, return True (program already trunning, so main() doesn't start).
    #Otherwise delete pid file, create new one with updated pid entry and return False (old process is dead, so loading can resume).
    
    currentProc = Process()
    print ('PsUtil info:')
    print ("ProcName:", currentProc.name(), "id:", currentProc.pid,  "status:", currentProc.status())
    print ("Proc children:", currentProc.children())
    print ("ProcParent:", currentProc.parent(),)
    print("Full path:", Process().exe())
    print("Current working directory:", currentProc.cwd())
     
    if not os.path.exists('pid'):
        print ("Pid file not found, creating pid file & loading")
        with open("pid", "a") as pidFile:
            newLine=str(currentProc.pid)+'\n'
            pidFile.write(newLine)
            pidFile.close()
            return False
    else:
        print ("")
        pidFile = open ( 'pid',"r" )
        lineList = pidFile. readlines()
        pidFile. close()
        lastEntry = int(lineList[len(lineList)-1])
        del lineList
        print ("Pid file found, last entry is:", lastEntry)

        if pid_exists(lastEntry):
            if 'python' in Process(lastEntry).name():
                print ("Program instance with pid {} already running\nExiting...".format(lastEntry))
                return True
        else:
            print ("Found earlier instance with pid {} but it's not running".format(lastEntry))
            if os.path.isfile('pid'):
                os.remove('pid') 
            with open("pid", "a") as pidFile:
                newLine=str(currentProc.pid)+'\n'
                pidFile.write(newLine)
                pidFile.close()
            return False


def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    
    systemTrayIcon = SystemTrayIcon()
    systemTrayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__': 
 
    if (alreadyRunnigPU("ttasm-desktop-app")):
        print ("Goodbye")
    else:
        print ('Loading')
        main()