import socket
import json

HOST = "127.0.0.1"
PORT = 5002
PASS_MARK = 50

def evaluate(marks):
    total = sum(marks)
    average = total / len(marks)
    result = "PASS" if all(mark >= PASS_MARK for mark in marks) else "FAIL"
    # A single student's rank is 1 in this simple standalone example.
    return {
        "marks": marks,
        "total": total,
        "average": round(average, 2),
        "result": result,
        "rank": 1
    }

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Marks server listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    with conn:
        raw = conn.recv(4096).decode()
        data = json.loads(raw)
        marks = data["marks"]
        if not marks or any(not isinstance(m, (int, float)) or m < 0 or m > 100 for m in marks):
            response = {"error": "Enter marks between 0 and 100."}
        else:
            response = evaluate(marks)
        conn.sendall(json.dumps(response).encode())
