import socket
from threading import Thread
from datetime import datetime
from time import sleep
from history import *
from authorization import *

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9091
sep = "<SEP>"

def listen():
    while True:
        message = sock.recv(1024).decode()
        print(message)


if __name__ == "__main__":
    # Connection to server
    sock = socket.socket()
    sock.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to {SERVER_HOST}:{SERVER_PORT}")
    # name = input("Input your name: ")
    while True:
        name = auto()
        if name:
            print("Success!!!")
            break
        print("Incorrect name or password")

    # Making a thread for listening to messages
    t = Thread(target=listen)
    t.daemon = True
    t.start()

    print("Greet everyone in the chat room")
    while True:

        to_send = input()
        if to_send == "q":
            break
        date_now = datetime.now().strftime("%d.%m.%y %H:%M:%S")

        write_message(date_now, name, to_send)

        to_send = f"[{date_now}] {name}{sep}{to_send}"
        sock.send(to_send.encode())

    sock.close()


