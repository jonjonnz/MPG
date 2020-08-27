import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.102"  # IP of the server we need to connect
        self.port = 5555  # Port of the server
        self.address = (self.server, self.port)  # Combined address of the server
        self.player = self.connect()

    def get_client(self):
        return self.player

    def connect(self):
        try:
            # Connecting to address and receiving back object from the server
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(2048))
        except Exception as err:
            print(err)
            pass

    def send(self, data):
        try:  # Sending the server an object and receiving something back
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except Exception as err:
            print(err)
