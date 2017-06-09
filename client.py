import json
import socket
import threading
import sys


SERVER_IP = '127.0.1.1'
SERVER_ACCESS_PORT = 50000
CHUNK_SIZE = 2


class Client():
    """ Class that handles all client side communication.
        It initialy connects to server just to get this client's dedicated port number,
        then discards initial socket. Communication is continued on dedicated port with new socket """

    def __init__(self, server_ip, server_access_port):
        self.server_ip = server_ip
        self.server_access_port = server_access_port
        self.initial_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dedicated_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):
        dedicated_port = int(self.get_dedicated_port())

        self.initial_sock.close()
        print("Connection with {} closed".format(self.server_access_port))

        self.dedicated_conection(self.dedicated_sock, self.server_ip, dedicated_port)


    def get_dedicated_port(self):
        """ Connect to server, receive dedicated port number and return it """
        self.initial_sock.connect((self.server_ip, self.server_access_port))
        print("Conected to {}:{}".format(SERVER_IP, SERVER_ACCESS_PORT))

        new_port = self.receive_message(self.initial_sock)
        print("Dedicated port is {}".format(new_port))

        return (new_port)


    def receive_message(self, sock):
        """ Collect arriving message on given socket, decode it and remove null char from end """

        data = []
        while (True):
            data_chunk = sock.recv(CHUNK_SIZE)
            data_decoded = data_chunk.decode()
            data.append(data_decoded)

            # null char is used to signal the end of message
            if data_decoded[-1] == '\x00':
                break

        total_data = ''.join(data)[:-1]
        return (total_data)


    def send_message(self, sock, message):
        """ Send decoded message through given socket with appended null char """

        # null char is used to signal the end of message
        message = message + '\x00'
        sock.send(message.encode())


    def dedicated_conection(self, sock, server_ip, dedicated_port):
        """ Create new connection with dedicated port, and send user input to server """

        print('Trying connection on dedicated {}:{}'.format(server_ip, dedicated_port))
        try:
            sock.connect((server_ip, dedicated_port))
        except:
            print('Unexpected connection error, shutting down')
            sock.close()
            sys.exit()

        print("Connected to {}:{}".format(server_ip, dedicated_port))

        # Send user input to server, and read whatever server sends back. FOREVER!
        while True:
            test_message = raw_input('[DEDICATED PORT {}] enter your message: '.format(dedicated_port))
            self.send_message(sock, test_message)
            msg = self.receive_message(sock)
            print('[SERVER MESSAGE] here is your message reversed - <{}>'.format(msg))



if __name__ == '__main__':
    client = Client(SERVER_IP, SERVER_ACCESS_PORT)
    clientThread = threading.Thread(target=client.run)
    clientThread.start()
