from collections import deque
import socket
import threading

from utility import receive_message, send_message


ACCESS_PORT = 50002
SERVER_HOST = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_HOST)
CHUNK_SIZE = 2

# THIS IS SOLUTION FOR TESTING ONLY
# make a deque of 10 000 numbers to serve as our available ports pool
# get ports by calling available_ports.pop()
available_ports = deque(range(50001, 60000))



class DedicatedClientConnection():
    """ Class for handling dedicated connection with client, separated from main logic
        Should always be called with Thread wrapper """


    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):
        with self.sock as s:
            s.bind((self.ip, self.port))
            s.listen(1)
            print('[THREAD PORT {}] listening'.format(self.port))

            conn, (cli_ip, cli_port) = s.accept()
            print('[THREAD PORT {}] got connection from {}:{}'.format(self.port, cli_ip, cli_port))

            # Expect message from client, then send reversed message back. FOREVER!
            while True:
                client_msg = receive_message(conn)
                print('[THREAD PORT {}] got message - <{}>'.format(self.port, client_msg))

                reversed_msg = client_msg[::-1] # reverse message
                send_message(conn, reversed_msg)
                print('[THREAD PORT {}] sent back reversed message - <{}>'.format(self.port, reversed_msg))

class SwitchWorker():
    """ Switch worker will just listen form initial connections from client.
        On successfull conection it will send available dedicated port to client,
        create a dedicated socket with dedicated port on separate thread (using DedicatedClientConnection class)
        and move on to next client. All comunication will then be held on dedicated thread. """

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Initializing switch worker")


    def run(self):
        print("Switch worker running")
        with self.sock as s:
            s.bind((self.ip, self.port))
            s.listen(5)
            while True:
                conn, (cli_ip, cli_port) = s.accept()
                print('\n[SW] got connection from {}:{}'.format(cli_ip, cli_port))

                dedicated_port = available_ports.pop()
                server_response = str(dedicated_port)

                # Create dedicated separate thread for comunication with client
                print('[SW] preparing connection for port {}'.format(dedicated_port))
                dedicatedConnection = DedicatedClientConnection(self.ip, dedicated_port)
                dedicatedConnectionThread = threading.Thread(target=dedicatedConnection.run)
                dedicatedConnectionThread.start()

                # Send encoded dedicated port number to client
                print('[SW] sending port num {} to {}:{}'.format(server_response, cli_ip, cli_port))
                conn.send(server_response.encode())


if __name__ == "__main__":
    switchWorker = SwitchWorker(SERVER_IP, ACCESS_PORT)
    switchWorker.run()
