import json
import socket
from threading import Thread
from collections import deque

ACCESS_PORT = 50000
SERVER_HOST = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_HOST)
CHUNK_SIZE = 1024

available_ports = deque(range(50001, 60000))


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
                    conn, addr = s.accept()
                    print('CONNECTION VARIABLE', conn)



if __name__ == "__main__":
    switchWorker = SwitchWorker(SERVER_IP, ACCESS_PORT)
    switchWorker.run()
