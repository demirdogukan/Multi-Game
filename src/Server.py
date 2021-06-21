from Engine.Character import Player
import socket
import threading
import pickle


class Server(threading.Thread):
    # CONSTANT
    TCP_IP = '127.0.0.1'
    PORT = 8080
    BUFFER_SIZE = 2048
    _clients: list = []

    def __init__(self):
        self._id = -1
        self._players = [Player((300, 500), "p1", 100, 5),
                         Player((200, 400), "p2", 100, 3)]

    def run(self):
        _socket = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)
        _socket.bind((self.TCP_IP, self.PORT))
        _socket.listen()
        print("Waiting for connect....")

        while True:
            client, addr = _socket.accept()

            self._clients.append(client)
            self._id += 1

            print(f"{addr},{self._id} connected to the game")

            t2 = threading.Thread(target=self.send_current_pos,
                                  args=(client, self._id,))
            t2.start()

    def send_current_pos(self, client, playerid):
        client.sendall(pickle.dumps(self._players[playerid]))
        while True:
            try:
                data = pickle.loads(client.recv(self.BUFFER_SIZE * 4))
                if data is not None:
                    self._players[playerid] = data

                    if playerid == 0:
                        client.sendall(pickle.dumps(self._players[1]))
                    elif playerid == 1:
                        client.sendall(pickle.dumps(self._players[0]))

            except socket.error as e:
                print(e)
                break


if __name__ == "__main__":
    s = Server()
    s.run()
