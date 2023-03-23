import socket

HOST = "127.0.0.1"
PORT = 5123

c = socket.socket()
c.connect((HOST, PORT))

print(f"Connected {HOST}:{PORT}".format(HOST,PORT))
for i in range(100):
    msg = c.recv(1024)
    print(msg.decode())

c.close()