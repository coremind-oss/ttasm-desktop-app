# import socket
# 
# client_socket = socket.socket()
# 
# host = socket.gethostname()
# ip = socket.gethostbyname(host)
# 
# port = 5000
# 
# address = (ip, port)
# 
# client_socket.connect(address)
# 
# print(client_socket.recv(1024))
# 
# client_socket.close()

import socket
from pip._vendor.distlib.compat import raw_input
from builtins import bytes

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostname()

port = 5000

address = (ip,port)

client_socket.connect(address)

data = raw_input('#### Enter your password to pass server authentication and press enter:')

client_socket.send(data.encode('utf_8'))
  
print('### Password are sent...')
  
print(client_socket.recv(2048))
  
client_socket.close()



