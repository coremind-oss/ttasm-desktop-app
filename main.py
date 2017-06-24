import sys, os, requests
from PyQt5.QtWidgets import QApplication
import psutil
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256

from tray import SystemTrayIcon



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
    update_server_public_key(HTTP_PROTOCOL, SERVER_URL)
    check_client_key()
#     check_credentials()


def check_credentials():
    #Check if credentials file present. If so, show auto-filled login form, else go to sign up form.
    pass

def check_client_key(http_protocol = HTTP_PROTOCOL, server_url = SERVER_URL):
    if not os.path.exists('./clientdata'):
        os.makedirs('./clientdata')
    
    if not os.path.exists('./serverdata/client_RSA'):    
        cl_rsa = create_private_key()
     
    url = '{}://{}/client_key_hash/'.format(http_protocol, server_url)
    print (url)

    print('trying to send client key hash to server:', url) 
    files = {'file': open('./clientdata/client_RSA.hash', 'rb')}
    try:
        response = requests.post(url, files=files)
        print (response.text)
    except Exception as e:
        print (e)
    

def create_private_key():
    #Create new client RSA private key, public key and public key hash and store them to disk
    random_generator = Random.new().read
    cl_rsa = RSA.generate(2048, random_generator)
    with open('./clientdata/client_RSA', 'wb') as f:
        f.write(cl_rsa.exportKey())
    with open('./clientdata/client_RSA.pub', 'wb') as f:
        f.write(cl_rsa.publickey().exportKey())
    with open('./clientdata/client_RSA.hash', 'w') as f:
        f.write(SHA256.new(cl_rsa.publickey().exportKey()).hexdigest())
    
    print ('Client keys created')
    return cl_rsa

def update_server_public_key(http_protocol, server_url):
    #get server private key and store it in ./serverdata/server_id_rsa.pub
    
    if not os.path.exists('./serverdata'):
        os.makedirs('./serverdata')
    
    url = '{http_protocol}://{server_url}/public_key/'.format(
        server_url = server_url,
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
        print ('No response, server may be down')

def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    start_up()
    #try_to_login()
    systemTrayIcon = SystemTrayIcon()
    systemTrayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if alreadyRunnigPU():
        print ('Goodbye')
    else:
        print ('Loading')
        main()
