# Reg Chuhi, Vincent Digiovanni, Julian Moylan
# NSSA 220 Project 2
'''
This file acts as the main, where it executes the other three and writes the collected
data to an output file called "output.csv"
'''

from filter_packets import *
from packet_parser import *
from compute_metrics import *
import csv

# Loop through 4 nodes
results = [compute(parse(filter(i)), i) for i in range(1, 5)]

# Write the results to a CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i, result in enumerate(results, 1):
        stats = list(result)

        writer.writerow([f"Node {i}"])
        writer.writerow([])
        # Write the metrics
        writer.writerow(["Echo Requests Sent", "Echo Requests Received", "Echo Replies Sent", "Echo Replies Received"])
        writer.writerow([str(stat) for stat in stats[:4]])
        writer.writerow(["Echo Request Bytes Sent (bytes)", "Echo Request Data Sent (bytes)"])
        writer.writerow([str(stat) for stat in stats[4:6]])
        writer.writerow(["Echo Request Bytes Received (bytes)", "Echo Request Data Received (bytes)"])
        writer.writerow([str(stat) for stat in stats[6:8]])
        writer.writerow([])
        writer.writerow(["Average RTT (milliseconds)", str(stats[8])])
        writer.writerow(["Echo Request Throughput (kB/sec)", str(stats[9])])
        writer.writerow(["Echo Request Goodput (kB/sec)", str(stats[10])])
        writer.writerow(["Average Reply Delay (microseconds)", str(stats[11])])
        writer.writerow(["Average Echo Request Hop Count", str(stats[12])])

        # Add an extra empty line if it's not the last input
        if i != len(results):
            writer.writerow([])
