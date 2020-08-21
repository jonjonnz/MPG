import socket
from _thread import *

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


# Threading the clients to run multiple at the same time
def threaded_clients(client_connection):
    client_connection.send(str.encode("Connected"))
    reply = ''
    # Making the thread run infinitely
    while True:
        try:
            data = client_connection.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print('Disconnected')
                break
            else:
                print("Received: ", reply)
            client_connection.sendall(str.encode(reply))
        except Exception as err:
            print('Client disconnected', err)
            break
    print("Lost connection")
    client_connection.close()

# Constantly listening and accepting client connections
while True:
    client_conn, client_address = s.accept()
    print('Connected to: ', client_address)

    start_new_thread(threaded_clients, (client_conn,))
