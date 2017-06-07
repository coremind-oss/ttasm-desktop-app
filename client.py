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



############### This actually work :D

# import socket
# from pip._vendor.distlib.compat import raw_input
# from builtins import bytes
#  
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  
# ip = socket.gethostname()
#  
# port = 5000
#  
# address = (ip,port)
#  
# client_socket.connect(address)
#  
# data = raw_input('#### Enter your password to pass server authentication and press enter:')
#  
# client_socket.send(data.encode('utf_8'))
#    
# print('### Password are sent...')
#    
# print(client_socket.recv(2048))
#    
# client_socket.close()

########### example 05.06.2017.
 
import json
import socket

from pip._vendor.distlib.compat import raw_input

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
host = socket.gethostname()# localhost
 
port = 50001
    
socket_client.connect((host,port))
print('connected on: ', host,port)

print('Waiting to server reply:')
while True:
    message = raw_input('Your message is: ')

    dictionary = {
      'username': 'dalibor',
      'password': 'some_password',
      'token': 'dryucjq0eo8hfukzajcpsilaghcshizscplhzi',
      'other_data': {
        'bla':'bla',
      },
      'custom_message': message,
    }

    json_string = json.JSONEncoder().encode(dictionary) + '\x00'
    json_bytes = json_string.encode('utf_8')
    print('trying to execute socket_client.send(json_bytes)')
    socket_client.send(json_bytes)
    print('success')
#     socket_client.send(message.encode('utf_8'))
    
    reply_from_server = socket_client.recv(2048)
    print(reply_from_server.decode())
  
socket_client.close()
      




