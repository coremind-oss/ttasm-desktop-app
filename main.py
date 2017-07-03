import sys, os, requests
from PyQt5.QtWidgets import QApplication
import psutil
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256

from tray import SystemTrayIcon


# global SERVER_URL
# global HTTP_PROTOCOL

SERVER_URL = '127.0.0.1:8000'
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
    pass
#     update_server_public_key(HTTP_PROTOCOL, SERVER_URL)
#     current_user = 'luka'
#     current_password = '1234567a'
#     check_client_key(current_user)
#     check_credentials()


def check_credentials():
    #Check if credentials file present. If so, show auto-filled login form, else go to sign up form.
    pass

def check_client_key(current_user, http_protocol = HTTP_PROTOCOL, server_url = SERVER_URL):
    if not os.path.exists('./clientdata'):
        os.makedirs('./clientdata')
    
    if not os.path.exists('./clientdata/client_RSA'):    
        cl_rsa = create_private_key()
     
    #send client key server for comparing
    url = '{}://{}/client_key/'.format(http_protocol, server_url)
    pub_key = open('./clientdata/client_RSA.pub', 'r').read()
    print('trying to send client key to server:', url) 

    try:
        response = requests.post(url, data={'user' : current_user, 'pub_key': pub_key})
        print ('Client public key sent to server')
    except Exception as e:
        print (e)
    

# def create_private_key():
#     #Create new client RSA private key, public key and public key hash and store them to disk
#     random_generator = Random.new().read
#     cl_rsa = RSA.generate(2048, random_generator)
#     with open('./clientdata/client_RSA', 'wb') as f:
#         f.write(cl_rsa.exportKey())
#     with open('./clientdata/client_RSA.pub', 'wb') as f:
#         f.write(cl_rsa.publickey().exportKey())
#     with open('./clientdata/client_RSA.hash', 'w') as f:
#         f.write(SHA256.new(cl_rsa.publickey().exportKey()).hexdigest())
#     
#     print ('Client keys created')
#     return cl_rsa



def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    start_up()
    systemTrayIcon = SystemTrayIcon()
    systemTrayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if alreadyRunnigPU():
        print ('Goodbye')
    else:
        print ('Loading')
        main()
