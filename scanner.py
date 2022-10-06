import socket
from threading import Thread, Lock
from time import sleep
from progress.bar import IncrementalBar
from tqdm import tqdm

N = 2**16 

port_lock = Lock()


def main(n):   
    for port in range(256):
        sock = socket.socket()
        progress_bar.update()
        try:
            with port_lock:
                sock.connect(('127.0.0.1', port+n))
                print("Порт", port+n, "открыт")
        except:
            continue
        
t = [Thread(target=main, args=[i])
    for i in range(0, N, N//256)]

progress_bar = tqdm(N, desc="Progress bar")

[t1.start() for t1 in t]
