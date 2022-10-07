import socket
from threading import Thread
from authorization import *
from history import *

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 9090

client_sockets = set()

sep = "<SEP>"


def listen(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"!*! Client {cs} no longer connected")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(sep, ": ")

        for client_socket in client_sockets:
            client_socket.send(msg.encode())


if __name__ == "__main__":

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((SERVER_HOST, SERVER_PORT))
    sock.listen(10)
    print(f"!*! Start listening as {SERVER_HOST}: {SERVER_PORT}")
    write_empty_row()
    while True:
        conn, addr = sock.accept()


        print(f"!*! {addr} connected!")
        client_sockets.add(conn)
        t = Thread(target=listen, args=(conn,))
        t.daemon = True
        t.start()

    for cs in client_sockets:
        cs.close()
    sock.close()
