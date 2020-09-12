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
s.listen(6)
print("Server started (Waiting for connection)...")

# 6 Players per server
clients = [Player(0, 0, 0, 0, (0, 0, 255)), Player(0, 0, 50, 50, (0, 255, 0)), Player(0, 0, 50, 50, (0, 255, 0)),
           Player(0, 0, 50, 50, (0, 255, 0)), Player(0, 0, 50, 50, (0, 255, 0)), Player(0, 0, 50, 50, (0, 255, 0))]


# Threading the clients to run multiple at the same time
def threaded_clients(client_connection, client):
    client_connection.send(pickle.dumps(clients[client]))  # Send back current player on the first connection
    reply = []
    # Making the thread run infinitely
    while True:
        try:
            data = pickle.loads(client_connection.recv(2048))
            clients[client] = data
            if not data:
                print('Disconnected')
                break
            else:
                for i in range(6):
                    if i != client:
                        reply.append(clients[i])    # Add other players to reply except current client

            client_connection.sendall(pickle.dumps(reply))
            reply = []
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
