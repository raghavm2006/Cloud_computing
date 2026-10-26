PYTHON DISTRIBUTED SYSTEMS PRACTICALS — 11 EXPERIMENTS

Requirements:
- Python 3.10+ recommended.
- Experiments 1, 2, 3, 4, 6, and 9 use XML-RPC or sockets as noted.
- Run server programs in one terminal and client programs in another terminal.
- For local testing, use 127.0.0.1.

Files:
01_client_server_server.py / 01_client_server_client.py
02_marks_server.py / 02_marks_client.py
03_serialization_server.py / 03_serialization_client.py
04_file_stats_server.py / 04_file_stats_client.py
05_token_ring.py
06_temperature_server.py / 06_temperature_client.py
07_berkeley_algorithm.py
08_clock_drift.py
09_shopping_server.py / 09_shopping_client.py
10_lamport_clock.py
11_round_robin_scheduler.py

Notes:
- Python has no built-in Java-style RMI. Experiments 6 and 9 use XML-RPC to demonstrate remote method calls.
- These are educational localhost examples, not production-ready network services.
- Experiment 4 only permits files in the server's current directory, to avoid arbitrary file access.
