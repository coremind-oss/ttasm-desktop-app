# from _socket import SHUT_RDWR
# import socket
# 
# 
# server_socket = socket.socket()
# 
# host = socket.gethostname()
# ip = socket.gethostbyname(host)
# 
# port = 5000
# 
# address = (ip, port)
# 
# server_socket.bind(address)
# 
# server_socket.listen(1)
# 
# 
# try:
#     while True:
#         print('waiting for a client to connect on {}:{}'.format(ip, port))
#         conn, addr = server_socket.accept()
#         kwargs = {
#             'ip': addr[0],
#             'port': addr[1], 
#         }
#         print('---> I have connection on port {port} from this address {ip}:{port}'.format(**kwargs))
#         conn.send(b' you have been connected to our server')
#         
#         conn.close()
# except Exception as e:
#     print(e)
#     conn.close()
#     server_socket.shutdown(SHUT_RDWR)












############### This actually work :D

# import socket
#    
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    
# host = socket.gethostname()
#    
# ip = socket.gethostbyname(host)
#    
# port = 5000
#    
# address = (ip,port)
#    
# server_socket.bind(address)
#    
# server_socket.listen(1)
#    
# while True:
#     print('----> Waiting communication from {}:{}'.format(ip,port))
#     client,addr = server_socket.accept()
#     print('Accepted communication from IP: ',addr[0], ' and port: ', addr[1])
#     data = client.recv(2048)
#     d=data.decode()
#     print('----> We recieved from client this data: ', d)
#     print('Processing the data...')
#     if d == "password":
#         client.send(b'Your password is correct!')
#         print('----> Password was correct')
#     else:
#         client.send(b'Incorrect password')
#         print('----> This password was incorrect')
#         client.close()
  
  
  
  
    
    
################### Single threaded port scanner   

# import socket
#   
# soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   
# host = socket.gethostname()
# 
# ip = socket.gethostbyname(host)
#   
# def port_scener(port):
#     try:
#         soc.connect((ip,port))
#         return True
#     except:
#         return False
#       
# for port in range(1,60000):
#     if port_scener(port):
#         print('Port ',port,' is opened')
    

############## Multithreaded Threaded port scenner with workers

# import socket
# import threading
# from queue import Queue
# from multiprocessing.pool import worker
#  
# print_lock = threading.Lock()
#  
# target = 'localhost'
#  
# def port_scanner(port):
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         conn = sock.connect((target,port))
#         with print_lock:
#             print('Port: ',port,' is opened!!!')
#         conn.close()
#     except:
#         pass
#      
#      
# def threader():
#     while True:
#         worker = q.get()
#         port_scanner(worker)
#         q.task_done()
#  
# q = Queue()
#  
# for i in range(100):
#     t = threading.Thread(target=threader)
#     t.deamon = True
#     t.start()
#      
# for worker in range(1,60000):
#     q.put(worker)
#      
# q.join()


########### example 05.06.2017.

# import socket
# import socket
# 
# from pip._vendor.distlib.compat import raw_input
# 
# 
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# host = socket.gethostname()

# host = socket.gethostname()
#  
# ip = socket.gethostbyname(host)
#  
# port = 50000
#  
# server_socket.bind((ip, port))
#  
# server_socket.listen(1)
#  
# conn,addr = server_socket.accept()
#  
# print("Connection recieved by ",addr[0], ' on port: ',addr[1])
# while True:
#     data = conn.recv(2048)# amount of data to recieve from client
#     if data:
#         print('Received data on :', data.decode())# data context from client
#         reply = raw_input('Enter data from server: ')
#         conn.sendall(reply.encode('utf_8'))# sending a raw input to client to allow client to enter credentials
#          
#  
# conn.close()
    
    
#### Multithread example try 05.06.2017.

import socket
import threading
 
 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
host = socket.gethostname()
 
ip = socket.gethostbyname(host)
 
port = 40000
 
serv_socket.bind((ip,port))
 
serv_socket.listen(5)
 
def clientHandler():
    while True:  
        conn,addr = serv_socket.accept()
        print('Server host client on ', addr[0], ' on port: ',addr[1])
        data = []
        while (True):
            data_chunk = conn.recv(50)
            if data_chunk:
                data_decoded = data_chunk.decode()
                data.append(data_decoded)
                last_in_data_row = data[len(data)-1]
#                 print(last_in_data_row)
            else:
                break
         
        total_data = last_in_data_row.join(data)
        print('Data recieved from client is :', total_data)
        server_response = 'You succesfully passed your data'
        conn.send(server_response.encode('utf_8'))
 
  
for i in range(5):
    t = threading.Thread(target=clientHandler())
    t.start()
 
serv_socket.close()
        
    
########## 06.06.2017.       


# import socket
# 
# 
# port=50000
# ip = socket.gethostbyname(socket.gethostname())
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((ip, port))
# server_socket.listen(5)
# print("Server waiting for client...")
# client_socket, address = server_socket.accept()
# while (True):
#     data = client_socket.recv(2)
#     if (data):
#         data_decoded = data.decode()
#     else:
#         break
#         print('no data')
# # print ('\n***** Recieved data ---->\n',data_decoded,'\n')
# data_dictionary = eval(data_decoded)
# print('*** USERNAME: ',data_dictionary['username'])
# print('*** PASSWORD: ',data_dictionary['password'])
# print('*** TOKEN: ',data_dictionary['token'])



