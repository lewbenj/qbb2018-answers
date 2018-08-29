#!/usr/bin/env python3
import sys 

pc = {}
npc = {}

my_dist = 0

for i, line in enumerate(sys.stdin): 
    if i <= 5:   
        continue     # got rid of the header, and defined variables
    fields = line.rstrip("\r\n").split("\t")  
    read_type = fields[2]
    chromosome = fields[0]
    #gene_name = fields[9]
    gene_start = int(fields[3])
    gene_end = int(fields[4])
    find_pos = int(21378950)
    gene_ID = line.rstrip("\r\n").split(" ")[1]
    if read_type == "gene" and chromosome == "3R":
        if "protein_coding" in fields[8]:
            if find_pos < gene_start:
                my_dist = gene_start - find_pos
                pc[gene_ID] = my_dist 
            elif find_pos > gene_end:
                my_dist = find_pos - gene_end
                pc[gene_ID] = my_dist 
#for name, value in dictionary.items():
    #print(name, value)  to test dictionary 
              
# for the non-protein coding genes               
        elif read_type == "gene" and chromosome == "3R":
            if find_pos < gene_start:
                my_dist = gene_start - find_pos
                npc[gene_ID] = my_dist
            elif find_pos > gene_end:
                my_dist = find_pos - gene_end
                npc[gene_ID] = my_dist
                
pc_min = min(pc, key= pc.get)# minimum finder; min(dictionary, key = dictionary.get)
print(pc_min, pc[pc_min])  # to print; print(min_finder, dictionary[min finder]

npc_min = min(npc, key= npc.get) 
print(npc_min, npc[npc_min])



                
                
        