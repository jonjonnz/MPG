import socket
from _thread import *

server = "192.168.0.102"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except Exception as err:
    print(err)
s.listen()
print("Server started (Waiting for connection)...")


def threaded_clients(client_connection):
    client_connection.send(str.encode("Connected"))
    reply = ''
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


while True:
    client_conn, client_address = s.accept()
    print('Connected to: ', client_address)

    start_new_thread(threaded_clients, (client_conn,))
