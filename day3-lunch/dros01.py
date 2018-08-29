#!/usr/bin/env python3
import sys 



protein_coding = 0

for i, line in enumerate(sys.stdin):
    if i <= 5:   
        continue
    fields = line.rstrip("\r\n").split("\t")
    if "gene" in fields[2]:
        if "protein_coding" in fields[8]:
            protein_coding += 1
print(protein_coding)

#./dros01.py < BDGP6.Ensembl.81.gtf

    

        
        
        
        
        
