import socket
from threading import Thread, Lock
from time import sleep

N = 2**16 

port_lock = Lock()


def main(n):   
    for port in range(256):
        sock = socket.socket()
        try:
            # print(port+n)
            with port_lock:
                sock.connect(('127.0.0.1', port+n))
                print("Порт", port+n, "открыт")
        except:
            continue
        
t = [Thread(target=main, args=[i])
    for i in range(0, N, N//256)]

[t1.start() for t1 in t]
