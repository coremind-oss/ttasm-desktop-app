def receive_message(sock, chunk_size=1024):
    """ Collect arriving message on connection. Excpected message format is bytearray \
        with 9 bytes long header representing total message size in bytes."""

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
            first_chunk = False

        total_data += data_chunk

        if len(total_data) == decoded_bytes_int:
            break


    print ('total data is', total_data)
    print ('decoded bytes length {}'.format(decoded_bytes_int))
    print('message length sould be', decoded_bytes_int, type(decoded_bytes_int))

    return (total_data[9:])

def send_message(sock, message):
    """ Appends 9 bytes long header to message and sends it to sock as bytes  """

    print(message, type(message))


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

    sock.send(new_message)
