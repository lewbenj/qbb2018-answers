#!/usr/bin/env python3
import sys 

#./fly_base_genes.py fly.txt

my_dict = {}

for line in open(sys.argv[1]):
    if "DROME" in line:
        fields = line.rstrip("\r\n").split()
        if len(fields) == 4:
            print(fields[3] + "\t\t" + fields[2])
            

            
            
    
        