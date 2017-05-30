import socket

server_socket = socket.socket()

host = socket.gethostname()

port = 5000

add = (host,port)

server_socket.bind(add)

server_socket.listen(1)



while True:
    conn, addr = server_socket.accept()
    print('I have connection from this address', addr)
    conn.send(b' you have been connected to our server')
    
    conn.close()


