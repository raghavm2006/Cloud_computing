import socket
import pickle

HOST = "127.0.0.1"
PORT = 5003

data = {
    "name": input("Enter your name: "),
    "course": input("Enter your course: "),
    "marks": [int(x) for x in input("Enter marks separated by spaces: ").split()]
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(pickle.dumps(data))  # Serialization: object -> bytes
reply = pickle.loads(client.recv(4096))  # Deserialization: bytes -> object
client.close()

print("Reply from server:", reply)
