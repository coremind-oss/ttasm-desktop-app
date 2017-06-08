import json
import socket
import threading
from collections import deque

ACCESS_PORT = 50001
SERVER_HOST = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_HOST)
CHUNK_SIZE = 1024

available_ports = deque(range(50001, 60001))


class DedicatedClientConnection():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        with self.sock as s:
            s.bind((self.ip, self.port))
            s.listen(1)
            while True:
                conn, (cli_ip, cli_port) = s.accept()
                print('[T] GOT CONNECTION FROM {}:{}'.format(cli_ip, cli_port))


class SwitchWorker():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        with self.sock as s:
            s.bind((self.ip, self.port))
            s.listen(5)
            while True:
                conn, (cli_ip, cli_port) = s.accept()
                print('[SW] GOT CONNECTION FROM {}:{}'.format(cli_ip, cli_port))
                dedicated_port = available_ports.pop()
                server_response = "{}{}".format(str(dedicated_port), "\x00")
                conn.send(server_response.encode())

                dedicatedConnection = DedicatedClientConnection(self.ip, dedicated_port)
                dedicatedConnectionThread = threading.Thread(target=dedicatedConnection.run)
                dedicatedConnectionThread.start()




if __name__ == "__main__":
    switchWorker = SwitchWorker(SERVER_IP, ACCESS_PORT)
    switchWorker.run()
