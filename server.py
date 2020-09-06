import socket
from _thread import *
from player import Player
import pickle

# IP to which everyone will connect
server = "192.168.0.102"
port = 5555

# Creating a socket and binding it to the IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except Exception as err:
    print(err)
s.listen()
print("Server started (Waiting for connection)...")

clients = [Player(0, 0, 0, 0, (0, 0, 255)), Player(0, 0, 50, 50, (0, 255, 0))]


# Threading the clients to run multiple at the same time
def threaded_clients(client_connection, client):
    client_connection.send(pickle.dumps(clients[client]))
    # Making the thread run infinitely
    while True:
        try:
            data = pickle.loads(client_connection.recv(2048))
            clients[client] = data
            if not data:
                print('Disconnected')
                break
            else:
                if client == 1:
                    reply = clients[0]
                else:
                    reply = clients[1]

            client_connection.sendall(pickle.dumps(reply))
        except Exception as err:
            print('Client disconnected', err)
            break
    print("Lost connection")
    client_connection.close()


# Constantly listening and accepting client connections
current_client = 0
while True:
    client_conn, client_address = s.accept()
    print('Connected to: ', client_address)

    start_new_thread(threaded_clients, (client_conn, current_client))
    current_client += 1
