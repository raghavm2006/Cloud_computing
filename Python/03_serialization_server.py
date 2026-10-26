import socket
import pickle

HOST = "127.0.0.1"
PORT = 5003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Serialization server listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    with conn:
        received = conn.recv(4096)
        # Only unpickle data from trusted clients. Pickle is unsafe for untrusted input.
        obj = pickle.loads(received)
        print("Deserialized object:", obj)
        reply = {"status": "success", "received": obj}
        conn.sendall(pickle.dumps(reply))
