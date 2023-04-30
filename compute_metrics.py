# Reg Chuhi, Vincent Digiovanni, Julian Moylan
# NSSA 220 Project 2
'''
This file takes the parsed fields and computes certain statistics for each node
'''

# List of node IPs
node_IP_addresses = ["192.168.100.1", "192.168.100.2", "192.168.200.1", "192.168.200.2"]

# Keys for the stats list
stats_keys = ["requests_sent", "requests_received", "replies_sent", "replies_received", "total_echo_req_bytes_sent", "total_echo_req_bytes_received", "total_echo_data_bytes_sent", "total_echo_data_bytes_received", "avg_RTT", "echo_request_throughput", "echo_request_goodput", "avg_reply_delay", "avg_hops_per_echo_request"]


def compute(parsed_packets, node_num):
    # Initialize dict with values of 0
    stats = {key: 0 for key in stats_keys}

    # Vars to temp store stats
    rtt_sum = 0
    rtt_total = 0
    reply_delay_sum = 0
    reply_delay_total = 0
    hop_count = 0
    total_packets = 0
    previous_packet = None

    # Loop through the parsed packets
    for packet in parsed_packets:
        time = packet[0]
        src_IP = packet[1]
        dest_IP = packet[2]
        length = packet[3]
        type = packet[4]
        seq = packet[5]
        ttl = packet[6]

        # Determine requests and replies sent/received
        if type == 'request':
            stats["requests_sent" if node_IP_addresses[node_num - 1] == src_IP else "requests_received"] += 1
        elif type == 'reply':
            stats["replies_sent" if node_IP_addresses[node_num - 1] == src_IP else "replies_received"] += 1

        # Determine frame and payload sent/received bytes
        if node_IP_addresses[node_num - 1] == src_IP:
            stats["total_echo_req_bytes_sent"] += int(length)             # frame
            stats["total_echo_data_bytes_sent"] += (int(length) - 20)     # payload
        else:
            stats["total_echo_req_bytes_received"] += int(length)         # frame
            stats["total_echo_data_bytes_received"] += (int(length) - 20) # payload

        # Determine RTT and reply delay
        if previous_packet is not None and seq in previous_packet[5]:
            if src_IP == node_IP_addresses[node_num - 1]:
                rtt_sum += (float(time) - float(previous_packet[0]))
                rtt_total += 1
            else:
                reply_delay_sum += (float(time) - float(previous_packet[0]))
                reply_delay_total += 1

        # Determine avg hops
        hop_count += 3 if ttl != "128" else 1
        total_packets += 1

        previous_packet = packet

    # Determine the remaining stats
    stats["avg_RTT"] = (rtt_sum / rtt_total) * 1000
    stats["echo_request_throughput"] = (stats["total_echo_req_bytes_sent"] / 1000) / rtt_sum
    stats["echo_request_goodput"] = (stats["total_echo_data_bytes_sent"] / 1000) / rtt_sum
    stats["avg_reply_delay"] = (reply_delay_sum / reply_delay_total) * 1000000
    stats["avg_hops_per_echo_request"] = hop_count / total_packets

    # Return the stats dict values
    return stats.values()