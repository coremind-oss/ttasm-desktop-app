import json
import socket


SERVER_IP = '127.0.1.1'
SERVER_ACCESS_PORT = 50000


class ClientThread():
    def __init__(self, server_ip, server_access_port):
        self.server_ip = server_ip
        self.server_access_port = server_access_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.get_dedicated_port()

    def get_dedicated_port(self):
        self.sock.connect((self.server_ip, self.server_access_port))
        print("CONNECTED TO {}:{}".format(SERVER_IP, SERVER_ACCESS_PORT))

    def recieve_message(self, sock):
        pass

if __name__ == '__main__':
    clientThread = ClientThread(SERVER_IP, SERVER_ACCESS_PORT)
