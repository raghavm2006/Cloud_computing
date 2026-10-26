# Token Ring simulation using a list of processes.
processes = ["P1", "P2", "P3", "P4", "P5"]
token_index = 0
requests = {"P2", "P4"}  # Processes that want to enter the critical section.

print("Token Ring Simulation")
for step in range(10):
    process = processes[token_index]
    print(f"Token is with {process}")
    if process in requests:
        print(f"{process} enters the critical section.")
        print(f"{process} exits the critical section.")
        requests.remove(process)
    else:
        print(f"{process} does not need the critical section.")
    token_index = (token_index + 1) % len(processes)

print("Simulation complete.")
