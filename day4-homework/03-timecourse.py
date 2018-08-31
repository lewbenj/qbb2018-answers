#!/usr/bin/env python3
import sys 
import pandas as pd
import os 
import matplotlib.pyplot as plt 
#import numpy as np

#Usage: ./03-timecourse.py <t_name> <samples.csv> <ctab_dir>
#./03-timecourse.py FBtr0331261 ~/qbb2018/samples.csv ~/data/results/stringtie/
# Create a timecourse of a given transcript (FBtr0331261) for females 



def timecourse(sex):
    df = pd.read_csv(sys.argv[2])
    soi = df.loc[:, "sex"] == sex
    #print(soi) to check if working
    df = df.loc[soi,:]
    fpkms = []
    stages = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col="t_name")
    
    
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        stages.append(stage)
    return fpkms, stages

fpkms, stages= timecourse('female')
fpkms_m, stages= timecourse('male')

fig, ax = plt.subplots()
ax.plot(fpkms, "r", label= "female")
ax.plot(fpkms_m, "b", label= "male")
ax.set_title("Sxl")
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (RPKM)")
ax.set_xticklabels(stages, rotation=90)
plt.legend(bbox_to_anchor =(1.07, 0.5), loc=2, borderaxespad=0)
plt.tight_layout()
fig.savefig("homework.png", bbox_inches='tight')
plt.close(fig)

# plt.xticks(np.arange(0), ("10", "11", "12", "13", "14a", "14b", "14c", "14d")
# plt.tight_layout()
# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# fig.savefig("homework.png")
# plt.close(fig)