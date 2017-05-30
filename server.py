from _socket import SHUT_RDWR
import socket


server_socket = socket.socket()

host = socket.gethostname()
ip = socket.gethostbyname(host)

port = 5000

address = (ip, port)

server_socket.bind(address)

server_socket.listen(1)


try:
    while True:
        print('waiting for a client to connect on {}:{}'.format(ip, port))
        conn, addr = server_socket.accept()
        kwargs = {
            'ip': addr[0],
            'port': addr[1], 
        }
        print('---> I have connection on port {port} from this address {ip}:{port}'.format(**kwargs))
        conn.send(b' you have been connected to our server')
        
        conn.close()
except Exception as e:
    print(e)
    conn.close()
    server_socket.shutdown(SHUT_RDWR)

