def receive_message(sock, chunk_size=14):
    """ Collect arriving message on connection. Excpected message format is bytearray \
        with 9 bytes long header representing total message size in bytes."""

#    data = []
    total_data = b''
    first_chunk = True
    while (True):
        data_chunk = sock.recv(chunk_size)
        print ('recieved chunk')
        if first_chunk:
            print (first_chunk)
            # grab the first nine bytes, decode into a string
            message_header = data_chunk[:9].decode('utf-8')
            print ('message header is', message_header)
            decoded_bytes_int = int (message_header)
            print ()
            #print ('supposed message size integer is', decoded_bytes_int)
            first_chunk = False
        #data_decoded = data_chunk.decode()
#        data.append(data_chunk)
        total_data += data_chunk
        if len(total_data) == decoded_bytes_int:
            break
        # null char is used to signal the end of message

        # try:
        #     #if data_decoded[-1] == '\x00':
        #     if
        #         break
        # except:
        #     port = sock.getsockname()[1]
        #     print('[THREAD PORT {}] user disconected, closing connection'.format(port))
        #     sock.close()
        #     # sys.exit(-1)
        #
        #     # total_data = ''.join(data)[:-1]


    print ('total data is', total_data)
    # # grab the first nine bytes, decode into a string
    # decoded_bytes_length = total_data[:9].decode('utf-8')
    print ('decoded bytes length {}'.format(decoded_bytes_int))
    print('message length sould be', decoded_bytes_int, type(decoded_bytes_int))

    # cast the string into an integer
    #int_length = int(decoded_bytes_length)
    #print(int_length, type(int_length))

    return (total_data[9:])

def send_message(sock, message):
    """ Send decoded message through given connection with appended null char """

    print(message, type(message))

    # null char is used to signal the end of message
    if isinstance(message, str):
        message_bytes = bytearray(message, 'utf-8')
    else:
        message_bytes = message

    total_length = len(message_bytes) + 9
    header_string = '{:09d}'.format(total_length)
    header_bytes = bytearray(header_string, 'utf-8')

    new_message = header_bytes + message_bytes
    print ('new message is ', new_message)
    print ('message length in bytes is {}'.format(len(message_bytes)))

    #message = message + '\x00'
    sock.send(new_message)
