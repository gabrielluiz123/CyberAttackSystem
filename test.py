import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
a = "2|2 horas|PassJack".encode()
client.send(a)
client.close()