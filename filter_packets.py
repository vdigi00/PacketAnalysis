from scapy.all import *

def filter(node_num):
    cap_dir = "Captures/"
    fil_dir = "Filtered_Node_Files/"

    txt_filename = f'{cap_dir}Node{node_num}.txt'
    filtered_filename = f'{fil_dir}Node{node_num}_filtered.txt'

    # packets = rdpcap(pcap_filename)

    # filtered_packets = [p for p in packets if p.haslayer(ICMP) and p[ICMP].type in [8, 0]]
    # print(filtered_packets)
    # with open(filtered_filename, 'w') as f:
    #     f.write('source_ip,dest_ip,type\n')  # Write header line
    #     for p in filtered_packets:
    #         src_ip = p[IP].src
    #         dst_ip = p[IP].dst
    #         icmp_type = 'request' if p[ICMP].type == 8 else 'reply'
    #         f.write(f'{src_ip},{dst_ip},{icmp_type}\n')

    # with open(txt_filename, 'w') as f:
    #     f.write('source_ip,dest_ip,type\n')  # Write header line
    #     for p in packets:
    #         if p.haslayer(ICMP) and p[ICMP].type in [8, 0]:
    #             src_ip = p[IP].src
    #             dst_ip = p[IP].dst
    #             icmp_type = 'request' if p[ICMP].type == 8 else 'reply'
    #             f.write(f'{src_ip},{dst_ip},{icmp_type}\n')
    
    with open(txt_filename, 'r') as f, open(filtered_filename, 'w') as fw:
		# Loop over every line in the file
        for line in f:
			# Check if it's an ICMP message
            if("ICMP" in line):
				# Write the line to the output file
                fw.write(line)

    return filtered_filename

# for node_num in range(1, 5):
#     filter(node_num)