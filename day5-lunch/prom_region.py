#!/usr/bin/env python3
import sys 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


#Usage: ./prom_region ~/data/results/stringtie/SRR072893/t_data.ctab
#Determine approximate promoter region for each of the transcripts present in your SRR072893/t_data.ctab file. Save as .bed file.



ctab_file = open(sys.argv[1])


promoter_start = []
promoter_end = []

for i, line in enumerate(ctab_file):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    chro = fields[1]
    strand = fields[2]
    start = fields[3]
    end = fields[4]
    t_id = fields[5]
    if "+" in strand:
        if int(start) > 500:
            promoter_start = int(start) - 500
            promoter_end = int(start) + 500

    elif "-" in strand:
        if int(end) > 500:
            promoter_start = int(end) - 500
            promoter_end = int(end) + 500
        
    bed_order = [chro, str(promoter_start), str(promoter_end), t_id]
    print("\t".join(bed_order))




