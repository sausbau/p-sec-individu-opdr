import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.2.18', 5000))
s.listen()

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")