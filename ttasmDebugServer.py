# Simple tcp server that listens on port 1234 and sends some basic responses

import socket

print ("ttasm local tcp server")
reception = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName=socket.gethostname
hostIp = socket.gethostbyname(socket.gethostname())
receptionActiveConnections=0

receptionPort = 1234

availablePorts = [7000, 7001, 7002] #at some point we will have to mantain actual list of available ports, but for now here's this
hostAddress=(hostIp, receptionPort)
reception.bind(hostAddress)
reception.listen(1)

print ('Started listening on {}:{}'.format(hostIp, receptionPort))
client, clientAddress=reception.accept()
receptionActiveConnections+=1
print ('Got connection from {}:{}'.format(clientAddress[0], clientAddress[1]))

#send='Invalid data'
#send=send.encode(encoding='utf_8', errors='strict')
#client.send(send)

while True:
    data = client.recv(1024)
    print ('Recieved {} from the client'.format(data.decode()))
    print ("Proccessing data")
    if (data.decode()=='Nice data'):
        client.send('Server recieved satisfying data'.encode())
        print ('Proccessing done.\nReply sent')
    else:
         if (data.decode()=='disconnect'):

             client.send('Goodbye'.encode())
             print ('Exiting...')
             client.close()
             receptionActiveConnections-=1
             break
         else:
             client.send('Invalid data'.encode())
             print ('Proccessing done, invalid data\nReply sent')
