import socket
from time import sleep

msg = "hello!"
HOST = "127.0.0.1"
PORT = 5123

s = socket.socket()
s.bind((HOST, PORT))
s.listen(3)

while True:
    try:
        client, addr = s.accept()
        print(f"Connection from {addr}".format(addr))
        for i in range(100):
            client.send(msg.encode())
            sleep(0.5)
    except KeyboardInterrupt:
        client.close()