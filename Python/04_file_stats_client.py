import socket

HOST = "127.0.0.1"
PORT = 5004

filename = input("Enter filename stored in the server directory: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(filename.encode())
print(client.recv(4096).decode())
client.close()
