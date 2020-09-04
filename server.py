import socket
from _thread import *
import pickle
from game import Game

# IP to which everyone will connect
server = "192.168.1.103"
port = 5555

# Creating a socket and binding it to the IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except Exception as err:
    print(err)
s.listen()
print("Server started (Waiting for connection)...")


# Threading the clients to run multiple at the same time
def threaded_clients(client_connection):
    global number_of_games, game_dict
    client_connection.send(str.encode('connected'))
    # client_connection.send(pickle.dumps(clients[client]))
    # Making the thread run infinitely
    while True:
        game_mode = client_connection.recv(2048).decode()
        if game_mode:
            if game_mode == 'new':
                g = Game()

                number_of_games += 1
                game_dict.append[number_of_games] = g
                client_connection.send(pickle.dumps(g))
            elif game_mode == 'existing':
                client_connection.send(pickle.dumps(game_dict))

            else:
                print('error, disconnecting...... wrong input')
                client_connection.close()
    while True:
        try:
            data = pickle.loads(client_connection.recv(2048))
            # clients[client] = data
            if not data:
                print('Disconnected')
                break
            # else:
            #     if client == 1:
            #         reply = clients[0]
            #     else:
            #         reply = clients[1]
            #
            # client_connection.sendall(pickle.dumps(reply))
        except Exception as err:
            print('Client disconnected', err)
            break
    print("Lost connection")
    client_connection.close()


# Constantly listening and accepting client connections
game_dict = {}
number_of_games = 0
while True:
    client_conn, client_address = s.accept()
    print('Connected to: ', client_address)

    start_new_thread(threaded_clients, (client_conn,))
