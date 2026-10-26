# Clock A runs at 1000 ms per second.
# Clock B runs at 1010 ms per second (10 ms faster each second).
clock_a = 0
clock_b = 0

for second in range(1, 61):
    clock_a += 1000
    clock_b += 1010
    if second % 10 == 0:
        print(f"After {second:2} seconds: A={clock_a} ms, B={clock_b} ms, drift={clock_b - clock_a} ms")

print("Final difference after 1 minute:", clock_b - clock_a, "ms")
