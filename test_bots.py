import socket, threading, random, time, string
from utility import receive_message, send_message

SERVER_IP = '127.0.1.1'
SERVER_ACCESS_PORT = 50000
CHUNK_SIZE = 2

class Talkative_Bot():

    """ A talkative bot that will try to break Pekmen's server """

    vowels = list('aeiour')

    def __init__(self, server_ip, server_access_port, bot_num):

        self.bot_num=bot_num
        self.server_ip = server_ip
        self.server_access_port = server_access_port
        self.initial_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dedicated_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def gen_word(self, min, max):
    	word = ''
    	syllables = min + int(random.random() * (max - min))
    	for i in range(0, syllables):
    		word += self.gen_syllable()

    	return word.capitalize()


    def gen_syllable(self):
    	ran = random.random()
    	if ran < 0.333:
    		return self.word_part('v') + self.word_part('c')
    	if ran < 0.666:
    		return self.word_part('c') + self.word_part('v')
    	return self.word_part('v') + self.word_part('c') + self.word_part('v')


    def word_part(self, type):
    	if type is 'c':
            return random.sample([ch for ch in list(string.ascii_lowercase) if ch not in self.vowels], 1)[0]
            #return random.sample([ch for ch in list(['q', 'w', 's', 'g', 'h', 'z']) if ch not in self.vowels], 1)[0]
    	if type is 'v':
    		return random.sample(self.vowels, 1)[0]


    def run(self):
        dedicated_port = int(self.get_dedicated_port())
        self.initial_sock.close()
        print("Handshake with {} successful".format(self.server_access_port))
        self.dedicated_conection(self.dedicated_sock, self.server_ip, dedicated_port)


    def get_dedicated_port(self):
        """ Connect to server, receive dedicated port number and return it """
        self.initial_sock.connect((self.server_ip, self.server_access_port))
        print("Conected to {}:{}".format(SERVER_IP, SERVER_ACCESS_PORT))

        new_port = receive_message(self.initial_sock)
        print("Dedicated port is {}".format(new_port))

        return (new_port)

    def dedicated_conection(self, sock, server_ip, dedicated_port):
        """ Create new connection with dedicated port, and send user input to server """

        print('Trying to connect on dedicated {}:{}'.format(server_ip, dedicated_port))
        try:
            sock.connect((server_ip, dedicated_port))
        except:
            print('Unexpected connection error, shutting down')
            print(traceback.format_exc())
            sock.close()
            sys.exit()
        print("Connected to {}:{}, starting to talk".format(server_ip, dedicated_port))

        #Bother Pekmen. FOREVER!
        while True:
            word = self.gen_word(3,8)
            message='I am bot #{} and i say {}'.format(self.bot_num+1, word)
            #print ('Sending {} to server'.format(word))
            send_message(sock, message)
            msg = receive_message(sock)
            #print('[SERVER MESSAGE] here is your message reversed - <{}>'.format(msg))
            time.sleep(1)
            print ("Total bots sent:", threading.active_count()-1)


def release_bots(total_bots):
    for i in range (total_bots):
        print ('Sending bot')
        bot = Talkative_Bot(SERVER_IP, SERVER_ACCESS_PORT, i)
        bot_thread = threading.Thread(target=bot.run)
        bot_thread.start()
        time.sleep(.01)

release_bots(100)
