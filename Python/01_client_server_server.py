import socket

HOST = "127.0.0.1"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server listening on {HOST}:{PORT}")

while True:
    connection, address = server.accept()
    with connection:
        print("Connected by", address)
        message = connection.recv(1024).decode()
        if not message:
            continue
        print("Client:", message)
        connection.sendall(("Server received: " + message).encode())
