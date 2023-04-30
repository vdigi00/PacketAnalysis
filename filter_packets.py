# Reg Chuhi, Vincent Digiovanni, Julian Moylan
# NSSA 220 Project 2
'''
This file filters for ICMP data from raw txt files and outputs it to a filtered txt file
'''

def filter(node_num):
    cap_dir = "Captures/"
    fil_dir = "Filtered_Node_Files/"

    txt_filename = f'{cap_dir}Node{node_num}.txt'
    filtered_filename = f'{fil_dir}Node{node_num}_filtered.txt'
    
    with open(txt_filename, 'r') as f, open(filtered_filename, 'w') as fw:
		# Loop over every line in the file
        for line in f:
			# Check if it's an ICMP message
            if("ICMP" in line):
				# Write the line to the output file
                fw.write(line)

    return filtered_filename