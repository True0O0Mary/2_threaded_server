import socket
from threading import Thread
from authorization import *
from history import *
import csv
from time import sleep

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 9091

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


def quit_chat():
    for cs in client_sockets:
        cs.close()
    sock.close()


def stop_port():
    global client_sockets
    stop_conn = input("Input port number")
    client_sockets.remove(stop_conn)


def show_logs():
    with open("history.csv", "r") as file:
        reader = csv.reader(file)
        for time, name, message in reader:
            print(f"Time: {time}, username: {name}, message: {message}, ")


def clean_logs():
    with open("history.csv", "w") as file:
        pass


def clean_auto():
    with open("authorization.json", "w") as file:
        pass


def menu():
    act_dict = {1: quit_chat, 2: show_logs, 3: clean_logs, 4: clean_auto()}
    while True:
        try:
            act = int(input("1: Quit chat, 2: Show logs, 3: Clean logs, 4: Clean authorization file, 5: break"))
        except:
            print("Not int input")
        if act == 5:
            break
        try:
            act_dict[act]
        except:
            print("Incorrect number input")


if __name__ == "__main__":

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((SERVER_HOST, SERVER_PORT))
    sock.listen(10)
    print(f"!*! Start listening as {SERVER_HOST}: {SERVER_PORT}")
    write_empty_row()
    # listen_t = Thread(target=menu())
    # listen_t.start()
    while True:
        conn, addr = sock.accept()
        print(f"!*! {addr} connected!")
        client_sockets.add(conn)
        t = Thread(target=listen, args=(conn,))
        t.daemon = True
        t.start()
        # t.join()
        listen_t = Thread(target=menu())
        listen_t.daemon = True
        listen_t.start()
        sleep(2)
        continue


    for cs in client_sockets:
        cs.close()
    sock.close()
