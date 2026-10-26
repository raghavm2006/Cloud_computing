import socket
import json

HOST = "127.0.0.1"
PORT = 5002

raw = input("Enter marks separated by spaces (example: 78 65 91): ")
marks = [float(value) for value in raw.split()]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(json.dumps({"marks": marks}).encode())
response = json.loads(client.recv(4096).decode())
client.close()

if "error" in response:
    print(response["error"])
else:
    print("Marks:", response["marks"])
    print("Total:", response["total"])
    print("Average:", response["average"])
    print("Result:", response["result"])
    print("Rank:", response["rank"])
    print("Note: rank is 1 because this demo evaluates one student at a time.")
