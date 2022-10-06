import socket
import threading


def main():
    sock = socket.socket()
    sock.bind(('', 9090))  
    sock.listen(0)  
    conn, addr = sock.accept()
    print(addr)

    msg = ''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        conn.send(data)

    print(msg)
    conn.close()


t = threading.Thread(target=main)
t_lock = threading.Lock()
with t_lock:
    t.start()