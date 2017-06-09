import sys


def receive_message(sock, chunk_size=1024):
    """ Collect arriving message on connection, decode it and remove null char from end """

    data = []
    while (True):
        data_chunk = sock.recv(chunk_size)
        data_decoded = data_chunk.decode()
        data.append(data_decoded)

        # null char is used to signal the end of message

        try:
            if data_decoded[-1] == '\x00':
                break
        except:
            port = sock.getsockname()[1]
            print('[THREAD PORT {}] user disconected, closing connection'.format(port))
            sock.close()
            sys.exit(-1)

    total_data = ''.join(data)[:-1]
    return (total_data)


def send_message(sock, message):
    """ Send decoded message through given connection with appended null char """

    # null char is used to signal the end of message
    message = message + '\x00'
    sock.send(message.encode())