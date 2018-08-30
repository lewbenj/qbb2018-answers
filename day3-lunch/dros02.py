#!/usr/bin/env python3
import sys 


my_dict = {}

for i, line in enumerate(sys.stdin): 
    if i <= 5:   
        continue
    fields = line.rstrip("\r\n").split("\t") #from here and above, I got rid of the header and created fields by getting rid of the spaces and add tab delimeters
    if "gene" in fields[2]: 
        fields = line.rstrip("\r\n").split() # for the lines with "gene" get rid of the spaces and then add a white space delimeter
        gene_type = fields[17] # count through file to figure out what field number it should be 
        #print(gene_type) to test 
        if gene_type in my_dict:
            my_dict[gene_type] += 1
        # if gene_type in my_dict is seen before add 1
        else:
            my_dict[gene_type] = 1
        # if gene_type in my_dict not seen before give value of 1
                
for name, value in my_dict.items():  
    print(name, value)
    
        
            






#for line in open(sys.argv[2]): #sys.argv[2] because fly.txt is second argument
 #   if "DROME" in line:
  #      fields = line.rstrip("\r\n").split()
   #        my_dict1.update({fields[3] : fields[2]})