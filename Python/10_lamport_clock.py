# Demonstrates Lamport logical clocks for three processes.
events = [
    ("P1", "local event"),
    ("P1", "send message to P2"),
    ("P2", "receive message from P1"),
    ("P2", "local event"),
    ("P2", "send message to P3"),
    ("P3", "receive message from P2"),
    ("P3", "local event"),
]

clocks = {"P1": 0, "P2": 0, "P3": 0}
message_timestamps = {}
message_id = 0

print("Lamport Logical Clock")
for process, event in events:
    if event.startswith("receive"):
        source = "P1" if "P1" in event else "P2"
        received_time = message_timestamps[source]
        clocks[process] = max(clocks[process], received_time) + 1
    else:
        clocks[process] += 1

    if event.startswith("send"):
        message_id += 1
        message_timestamps[process] = clocks[process]

    print(f"{process}: {event} -> Lamport time {clocks[process]}")
