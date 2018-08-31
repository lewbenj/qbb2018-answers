#!/usr/bin/env python3
import sys 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


#Usage: ./prom_region ~/data/results/stringtie/SRR072893/t_data.ctab
#Determine approximate promoter region for each of the transcripts present in your SRR072893/t_data.ctab file. Save as .bed file.




#coi = ["chr", "start", "end", "t_name"]
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
        promoter_start = float(start) - 500
        promoter_end = float(start) + 500

    elif "-" in strand:
        promoter_start = float(end) - 500
        promoter_end = float(end) + 500
        
    bed_order = [chro, str(promoter_start), str(promoter_end), t_id]
    print("\t".join(bed_order))




# df = pd.read_csv(sys.argv[1], sep = "\t")
# #width = df.loc[:, "end"] - df.loc[:, "start"] + 1
# promoter_start = 0
# promoter_end = 0
# df1 = df.assign(score=promoter_start)
# df2 = df.assign(score=promoter_end)
# #suggest use .loc over [] or can use (i).loc [] to separate by index
# coi = ["chr", "start", "end", "t_name"]
#
# for i in coi:
#     if "strand" == "+":
#         promoter_start = df.loc[:, "start"] + 500
#         promoter_end = df.loc[:, "start" ] + 500
#
#     elif "strand" in "+":
#         promoter_start = df.loc[:, "end"] - 500
#         promoter_end = df.loc[:, "end" ] - 500
#
# df2.loc[:, coi[0: 5]].to_csv(sys.stdout, sep="\t", index=False )





#df = pd.read_csv(sys.argv[1], index_col=0)

# my_dist = 0
# if find_pos < gene_start:
# my_dist = gene_start - find_pos
# elif find_pos > gene_end:
# my_dist = find_pos – gene_end