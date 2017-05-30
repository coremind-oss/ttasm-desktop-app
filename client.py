import socket

client_socket = socket.socket()

host = socket.gethostname()
ip = socket.gethostbyname(host)

port = 5000

address = (ip, port)

client_socket.connect(address)

print(client_socket.recv(1024))

client_socket.close()
