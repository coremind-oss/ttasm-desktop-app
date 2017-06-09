import json
import sys
import socket
import threading
from collections import deque


ACCESS_PORT = 50000
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
                client_msg = self.receive_message(conn)
                print('[THREAD PORT {}] got message - <{}>'.format(self.port, client_msg))

                reversed_msg = client_msg[::-1] # reverse message
                self.send_message(conn, reversed_msg)
                print('[THREAD PORT {}] sent back reversed message - <{}>'.format(self.port, reversed_msg))


    def receive_message(self, connection):
        """ Collect arriving message on connection, decode it and remove null char from end """

        data = []
        while (True):
            data_chunk = connection.recv(CHUNK_SIZE)
            data_decoded = data_chunk.decode()
            data.append(data_decoded)

            # null char is used to signal the end of message

            try:
                if data_decoded[-1] == '\x00':
                    break
            except:
                print('[THREAD PORT {}] user disconected, closing connection'.format(self.port))
                connection.close()
                available_ports.appendleft(self.port)
                sys.exit()

        total_data = ''.join(data)[:-1]
        return (total_data)


    def send_message(self, connection, message):
        """ Send decoded message through given connection with appended null char """

        # null char is used to signal the end of message
        message = message + '\x00'
        connection.send(message.encode())



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
                server_response = "{}{}".format(str(dedicated_port), '\x00')

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
