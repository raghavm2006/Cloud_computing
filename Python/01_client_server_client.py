import socket

HOST = "127.0.0.1"
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
message = input("Enter a message: ")
client.sendall(message.encode())
reply = client.recv(1024).decode()
print("Reply from server:", reply)
client.close()
