# Reg Chuhi, Vincent Digiovanni, Julian Moylan
# NSSA 220 Project 2
'''
This file parses the filtered txt file and extracts the time, source IP, destination IP, 
packet length, packet type, sequence and time-to-live fields
'''

def parse(filtered_file):
    parsed_packets = []

    with open(filtered_file, 'r') as f:
        packet = f.readline()

        while packet:
            packet_data = packet.split()
            # if len = 10, there is a destination unreachable error
            if len(packet_data) != 10:
                parsed_packet_data = []

                # Extract the time, src_IP, dest_IP, length, packet type, sequence, ttl and add to parsed data
                for i in range(1, 12):
                    if i in (4,6,7,9): continue
                    if i in (10,11): 
                        parsed_packet_data.append(packet_data[i][4:])
                    else: 
                        parsed_packet_data.append(packet_data[i])

                # Add the formatted data list to the parsed_packets list
                parsed_packets.append(parsed_packet_data)
                
            # Read in the next line
            packet = f.readline()

    # return the parsed_packets
    return parsed_packets