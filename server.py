import json
import socket
import threading
from collections import deque

ACCESS_PORT = 50009
SERVER_HOST = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_HOST)
CHUNK_SIZE = 2

available_ports = deque(range(50001, 56666))


class DedicatedClientConnection():
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
            while True:
                client_msg = self.receive_message(conn)
                print('[THREAD PORT {}] got message - {}'.format(self.port, client_msg))
                self.send_message(conn, '[SERVER MESSAGE] here is your message reversed - ' + client_msg[::-1])


    def receive_message(self, connection):
        data = []
        while (True):
            data_chunk = connection.recv(CHUNK_SIZE)
            data_decoded = data_chunk.decode()
            data.append(data_decoded)
            if data_decoded[-1] == '\x00':
                break

        total_data = ''.join(data)[:-1]
        return (total_data)


    def send_message(self, connection, message):
        message = message + '\x00'
        connection.send(message.encode())


class SwitchWorker():
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
                print('[SW] sending port num {} to {}:{}'.format(server_response, cli_ip, cli_port))
                conn.send(server_response.encode())

                print('[SW] preparing connection for port {}'.format(dedicated_port))
                dedicatedConnection = DedicatedClientConnection(self.ip, dedicated_port)
                dedicatedConnectionThread = threading.Thread(target=dedicatedConnection.run)
                dedicatedConnectionThread.start()


if __name__ == "__main__":
    switchWorker = SwitchWorker(SERVER_IP, ACCESS_PORT)
    switchWorker.run()
