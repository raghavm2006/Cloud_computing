# Round-robin assignment of tasks to two worker nodes.
tasks = [
    ("Task-1", 4),
    ("Task-2", 2),
    ("Task-3", 7),
    ("Task-4", 3),
    ("Task-5", 5),
    ("Task-6", 1),
]

workers = {
    "Worker-1": {"available_at": 0, "count": 0},
    "Worker-2": {"available_at": 0, "count": 0},
}
worker_names = list(workers)

print("Round Robin Task Scheduler")
for index, (task_name, processing_time) in enumerate(tasks):
    worker_name = worker_names[index % len(worker_names)]
    worker = workers[worker_name]

    start_time = worker["available_at"]
    completion_time = start_time + processing_time
    worker["available_at"] = completion_time
    worker["count"] += 1

    print(
        f"{task_name} (processing={processing_time}) -> {worker_name}; "
        f"start={start_time}, completion={completion_time}"
    )

print("\\nNumber of tasks assigned:")
for worker_name, worker in workers.items():
    print(f"{worker_name}: {worker['count']} tasks")
