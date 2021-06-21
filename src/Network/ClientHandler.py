import pickle
import socket


class ClientManager:
    # is being used currently
    TC_IP = '127.0.0.1'
    PORT = 8080
    BUFFER_SIZE = 2048

    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.p = self.connect()

    def get_player1(self):
        return self.p

    def connect(self):
        self._socket.connect((self.TC_IP,  self.PORT))
        return pickle.loads(self._socket.recv(self.BUFFER_SIZE))

    def send_data(self, data):
        try:
            self._socket.send(pickle.dumps(data))
            recv_data = pickle.loads(self._socket.recv(self.BUFFER_SIZE * 10))
            return recv_data
        except socket.error:
            print("Something went wrong wih socket..")
            self._socket.close()
