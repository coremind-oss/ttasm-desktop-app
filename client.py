import json
import socket
import threading


SERVER_IP = '127.0.1.1'
SERVER_ACCESS_PORT = 50001
CHUNK_SIZE = 5


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
        print("CONNECTED TO {}:{}".format(SERVER_IP, SERVER_ACCESS_PORT))
        new_port = self.receive_message(self.initial_sock)
        print("NEW PORT IS {}".format(new_port))
        self.initial_sock.close()
        return (new_port)

    def receive_message(self, sock):
        data = []
        while (True):
            data_chunk = sock.recv(CHUNK_SIZE)
            data_decoded = data_chunk.decode()
            data.append(data_decoded)
            if data_chunk[-1] == '\x00':
                break
        data = data[:-1]
        return (''.join(data))

    def dedicated_conection(self, sock, server_ip, dedicated_port):
        sock.connect((server_ip, dedicated_port))
        print("[DEDICATED] CONNECTED TO {}:{}", server_ip, dedicated_port)



if __name__ == '__main__':
    client = Client(SERVER_IP, SERVER_ACCESS_PORT)
    clientThread = threading.Thread(target=client.run)
    #clientThread.daemon = True
    clientThread.start()
