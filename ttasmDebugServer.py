# Simple tcp server that listens on port 1234 and sends some basic responses

import socket

print ("Ttasm local tcp server")
reception = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName=socket.gethostname
hostIp = socket.gethostbyname(socket.gethostname())


receptionPort = 1234

availablePorts = [7000, 7001, 7002] #at some point we will have to mantain actual list of available ports, but for now here's this
hostAddress=(hostIp, receptionPort)
reception.bind(hostAddress)
reception.listen(1)

print ('Started listening on {}:{}'.format(hostIp, receptionPort))
client, clientAddress=reception.accept()

#make client socket reusable (doesn't actually work)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print ('Got connection from {}:{}'.format(clientAddress[0], clientAddress[1]))

#start listening loop
while True:
    data = client.recv(1024)
    print ('Recieved {} from the client'.format(data.decode()))
    print ("Proccessing data")
    if (data.decode()=='Nice data'):
        client.send('Server recieved satisfying data'.encode())
        print ('Nice data recieved.\nReply sent')
        client.close()
        break
    else:
         if (data.decode()=='disconnect'):

             client.send('Goodbye'.encode())
             print ('Exiting...')
             client.close()

             break
         else:
             try:
                 client.send('Your client sent invalid data'.encode())
                 print ('Invalid data form {}:{} recieved, exiting...'.format(clientAddress[0], clientAddress[1]))
                 client.close()
                 
                 break
             except Exception as e:
                print (e)
