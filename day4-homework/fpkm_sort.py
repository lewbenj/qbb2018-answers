#!/usr/bin/env python3
import sys 
import pandas as pd
import os 
import matplotlib.pyplot as plt 

#Usage: ./fpkm_sort.py <samples.csv> <ctab_file> <sex>
#./fpkm_sort.py ~/qbb2018/samples.csv ~/data/results/stringtie/
# Create a timecourse of a given transcript (FBtr0331261) for females 

df = pd.read_csv(sys.argv[1])
#soi = df.loc[:, "sex"] == "female"
#print(soi) to check if working
#df = df.loc[soi,:]

collated = {}
for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
    ctab_df = pd.read_table(filename, index_col="t_name")
    
    
    collated[sex + "_" + stage] = ctab_df.loc[:, "FPKM"]
    dfcollated = pd.DataFrame(collated)
    #fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
print(dfcollated)
    

# fig, ax = plt.subplots()
# ax.plot(fpkms)
# fig.savefig("timecourse.png")
# plt.close(fig)




