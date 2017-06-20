import sys


def receive_message(sock, chunk_size=1024):
    """ Collect arriving message on connection, decode it and remove null char from end """

    data = []
#     while (True):
    data_chunk = sock.recv(chunk_size)
    #data_decoded = data_chunk.decode()
    data.append(data_chunk)

        # null char is used to signal the end of message

#         try:
#             if data_decoded[-1] == '\x00':
#                 break
#         except:
#             port = sock.getsockname()[1]
#             print('[THREAD PORT {}] user disconected, closing connection'.format(port))
#             sock.close()
#             sys.exit(-1)

    #total_data = ''.join(data)[:-1]
    total_data = data_chunk
#     for chunk in data:
#         total_data += chunk
    
    print ('total data is', total_data)
    # grab the first nine bytes, decode into a string
    decoded_bytes_length = total_data[:9].decode('utf-8')
    print ('decoded bytes length {}', decoded_bytes_length)
    print('message length sould be', decoded_bytes_length, type(decoded_bytes_length))
    
    # cast the string into an integer
    #int_length = int(decoded_bytes_length)
    #print(int_length, type(int_length))

    return (total_data)

def send_message(sock, message):
    """ Send decoded message through given connection with appended null char """

    # null char is used to signal the end of message
    message_bytes = bytearray(message, 'utf-8')

    total_length = len(message_bytes) + 9
    length_string = '{:09d}'.format(total_length)
    length_bytes = bytearray(length_string, 'utf-8')
    
    new_message = length_bytes + message_bytes
    print ('new message is ', new_message)
    print ('message length in bytes is {}'.format(len(message_bytes)))
    
    #message = message + '\x00'
    sock.send(new_message)
    
    
    
    
    