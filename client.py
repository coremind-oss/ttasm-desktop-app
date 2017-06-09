import json
import socket
import threading
import sys


SERVER_IP = '127.0.1.1'
SERVER_ACCESS_PORT = 50009
CHUNK_SIZE = 2


class Client():
    def __init__(self, server_ip, server_access_port):
        self.server_ip = server_ip
        self.server_access_port = server_access_port
        self.initial_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dedicated_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):
        dedicated_port = int(self.get_dedicated_port())
        self.dedicated_conection(self.dedicated_sock, self.server_ip, dedicated_port)


    def get_dedicated_port(self):
        self.initial_sock.connect((self.server_ip, self.server_access_port))
        print("Conected to {}:{}".format(SERVER_IP, SERVER_ACCESS_PORT))

        new_port = self.receive_message(self.initial_sock)
        print("Dedicated port is {}".format(new_port))

        self.initial_sock.close()
        print("Connection with {} closed".format(self.server_access_port))

        return (new_port)


    def receive_message(self, sock):
        data = []
        while (True):
            data_chunk = sock.recv(CHUNK_SIZE)
            data_decoded = data_chunk.decode()
            data.append(data_decoded)
            if data_decoded[-1] == '\x00':
                break

        total_data = ''.join(data)[:-1]
        return (total_data)


    def send_message(self, sock, message):
        message = message + '\x00'
        sock.send(message.encode())


    def dedicated_conection(self, sock, server_ip, dedicated_port):
        print('[DEDICATED] trying connection on {}:{}'.format(server_ip, dedicated_port))
        try:
            sock.connect((server_ip, dedicated_port))
        except:
            print('[DEDICATED] unexpected error, shutting down')
            sock.close()
            sys.exit()

        print("[DEDICATED] connected to {}:{}".format(server_ip, dedicated_port))
        while True:
            test_message = raw_input('[DEDICATED PORT {}] enter your message: '.format(dedicated_port))
            self.send_message(sock, test_message)
            print('[DEDICATED PORT {}] sent message - {}'.format(dedicated_port, test_message))
            msg = self.receive_message(sock)
            print(msg)



if __name__ == '__main__':
    client = Client(SERVER_IP, SERVER_ACCESS_PORT)
    client.run()
    clientThread = threading.Thread(target=client.run)
    clientThread.daemon = True
    clientThread.start()
