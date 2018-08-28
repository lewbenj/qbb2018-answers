#!/usr/bin/env python3
import sys 

# ~/data/results/stringtie/SRR072893/t_data.ctab fly.txt

#create dictionary to store the fly gene id numbers and AC
my_dict1 = {} 


#imported code from fly_base_genes.py

for line in open(sys.argv[2]): #sys.argv[2] because fly.txt is second argument
    if "DROME" in line:
        fields = line.rstrip("\r\n").split()
        if fields[-1].startswith("FBgn"):
            my_dict1.update({fields[3] : fields[2]})
#print(my_dict1) to test (This code searched for the lines with DROME in the reverse index) 

#now, get the ctab file. This will generate matches between the ctab file and the fly base genes
for line in open(sys.argv[1]):
    if "FBgn" in line:
        fields = line.rstrip("\r\n").split()
        if fields[8] in my_dict1.keys():
            print(my_dict1[fields[8]], "\t", line)
        else:
            print("No match", "\t", line) # this places all the No matches at the end.
            



    
    
    
    
    
    

    
        
    
    
    
    