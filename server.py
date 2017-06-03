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

import socket
  
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
host = socket.gethostname()

ip = socket.gethostbyname(host)
  
def port_scener(port):
    try:
        soc.connect((ip,port))
        return True
    except:
        return False
      
for port in range(1,60000):
    if port_scener(port):
        print('Port ',port,' is opened')
    

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
    
 
        
    
        
    

