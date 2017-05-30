import socket

client_socket = socket.socket()

host = socket.gethostname()

port = 5000

address=(host,port)

client_socket.connect(address)

print(client_socket.recv(1024))

client_socket.close()



