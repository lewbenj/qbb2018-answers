#!/usr/bin/env python3
import sys 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#Usage: ./merge_fpkms.sh <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen>
#./merge_fpkms.py x ~/data/results/stringtie/SRR072893/t_data.ctab ~/data/results/stringtie/SRR072915/t_data.ctab ~/data/results/stringtie/SRR072909/t_data.ctab 


fpkms_dict = {}

for i in range(2,len(sys.argv)):
    name1 = sys.argv[i].split(os.sep)[-2]
    fpkm = pd.read_csv(sys.argv[i], sep = "\t", index_col = "t_name").loc[:, "FPKM"]
    fpkms_dict[name1] = fpkm 
#print(fpkms_dict) #to test dictionary 
fpkms_df = pd.DataFrame(fpkms_dict)
#print(fpkms_df) to test if columns made
fpkms_df.sum = fpkms_df.sum(axis=1)
# print(fpkms_df.sum) #to check if it worked

roi_fpkm = fpkms_df.sum > float(sys.argv[1])
#print(roi_fpkm)
transcript = fpkms_df.sum.index[roi_fpkm == True] #finds the given element in the list and return it
print(transcript)



