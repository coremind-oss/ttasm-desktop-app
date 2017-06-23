import sys, os, requests
from PyQt5.QtWidgets import QApplication
import psutil
from Crypto.PublicKey import RSA

from tray import SystemTrayIcon



SERVER_IP = '127.0.0.1'
SERVER_ACCESS_PORT = '8000'
HTTP_PROTOCOL = 'HTTP' # http_protocol would represent HTTP or HTTPS


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
    print('Current working directory:', currentProc.cwd())
     
    if not os.path.exists('./pid'):
        print ('Pid file not found, creating pid file')
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


def start_up():
    update_server_public_key(HTTP_PROTOCOL, '{}:{}'.format(SERVER_IP, SERVER_ACCESS_PORT))
#     check_credentials()


def check_credentials():
    #Check if credentials file present. If so, show auto-filled login form, else go to sign up form.
    pass


def update_server_public_key(http_protocol, server_ip):
    #get server private key and store it in ./serverdata/server_id_rsa.pub
    
    if not os.path.exists('./serverdata'):
        os.makedirs('./serverdata')
    
    url = '{http_protocol}://{server_ip}/public_key/'.format(
        server_ip = server_ip,
        http_protocol = http_protocol,
    )
    print('trying to get the public key from:', url) 
    try:
        response = requests.get(url)
        print ('response text:', response.text)
        if response.status_code == 200:
            with open('./serverdata/server_id_rsa.pub', 'w') as file: 
                file.write(response.text)
                print ('server_id_rsa.pub aquired and stored as ./serverdata/server_id_rsa.pub')
        else:
            print ('Server failed to provide public key')
    except:
        print ('Something went wrong, server may be down')

def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    
    systemTrayIcon = SystemTrayIcon()
    start_up()
    systemTrayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if alreadyRunnigPU():
        print ('Goodbye')
    else:
        print ('Loading')
        main()
