import socket
from pathlib import Path

HOST = "127.0.0.1"
PORT = 5004
BASE_DIR = Path.cwd().resolve()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"File statistics server listening on {HOST}:{PORT}")
print("Place files to inspect in:", BASE_DIR)

while True:
    conn, addr = server.accept()
    with conn:
        filename = conn.recv(1024).decode().strip()
        # Only allow a simple filename inside the server's current directory.
        path = (BASE_DIR / filename).resolve()
        if path.parent != BASE_DIR or not path.is_file():
            response = "ERROR: File not found in server directory."
        else:
            content = path.read_text(encoding="utf-8", errors="replace")
            lines = len(content.splitlines())
            words = len(content.split())
            size = path.stat().st_size
            response = f"File: {path.name}\\nLines: {lines}\\nWords: {words}\\nSize: {size} bytes"
        conn.sendall(response.encode())
