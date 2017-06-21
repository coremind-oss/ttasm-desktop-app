from Crypto.PublicKey import RSA


def receive_message(sock, chunk_size=1):
    """ Collect arriving message on connection. Expected message format is bytearray \
        with 9 bytes long header representing total message size in bytes."""

    total_data = b''
    got_header = False

    while (True):
        data_chunk = sock.recv(chunk_size)
        print ('recieved chunk')
        total_data += data_chunk

        if len(total_data) >= 9:

            if not got_header :
                # grab the first nine bytes, decode into a string
                message_header = total_data[:9].decode('utf-8')
                print ('message header is', message_header)
                decoded_bytes_int = int (message_header)
                got_header = True

            if len(total_data) == decoded_bytes_int:
                    break

        # This helps with client disconnects
        if not data_chunk :
            break

    try:
        decoded_bytes_int
        print ('decoded bytes length {}'.format(decoded_bytes_int))
        print('message length sould be', decoded_bytes_int, type(decoded_bytes_int))
        return (total_data[9:])
    except:
        print ('Something went wrong while receiving')
        return (b'ReceiveError')




def send_message(sock, message):
    """ Send message through given connection with 9 byte header appended """

    if isinstance(message, str):
        message_bytes = bytearray(message, 'utf-8')
    else:
        message_bytes = message

    total_length = len(message_bytes) + 9
    header_string = '{:09d}'.format(total_length)
    header_bytes = bytearray(header_string, 'utf-8')

    new_message = header_bytes + message_bytes
    print ('new message is', new_message)
    print ('message length in bytes is {}'.format(len(message_bytes)))

    sock.send(new_message)

def encrypt_message (message, public_key):
    key = RSA.importKey(public_key)
    enc_data = key.encrypt(message.encode('utf-8'), 32)
    return enc_data[0]

def decrypt_message (message, private_key):
    key = RSA.importKey(private_key)
    dec_data = key.decrypt (message)
    return dec_data
