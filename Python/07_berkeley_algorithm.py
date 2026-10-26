# Simplified Berkeley clock synchronization simulation.
clocks = [100, 104, 98, 110]  # Times in seconds: master followed by three nodes.
master = clocks[0]

# Each node reports its offset from the master's clock.
offsets = [clock - master for clock in clocks]
average_offset = sum(offsets) / len(offsets)

print("Clock readings:", clocks)
print("Offsets from master:", offsets)
print("Average offset:", average_offset)

# The master sends each node the adjustment needed to reach the average time.
synchronized = [round(clock - (clock - master) + average_offset, 2) for clock in clocks]
print("Adjustment for each clock:", [round(average_offset - offset, 2) for offset in offsets])
print("Synchronized clock values (relative):", synchronized)
