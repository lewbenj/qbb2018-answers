#!/usr/bin/env python3
import sys 
import pandas as pd
import os 
import matplotlib.pyplot as plt 
#import numpy as np

#Usage: ./replicates.py <t_name> <samples.csv> <ctab_dir>
#./replicates.py FBtr0331261 ~/qbb2018/samples.csv ~/data/results/stringtie/
#./replicates.py FBtr0331261 ~/qbb2018/samples.csv ~/data/results/stringtie/ ~/qbb2018/replicates.csv
# Create a timecourse of a given transcript (FBtr0331261) for transcripts



def timecourse1(sex):
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


def timecourse2(sex):
    df = pd.read_csv(sys.argv[4])
    soi = df.loc[:, "sex"] == sex
    #print(soi) to check if working
    df = df.loc[soi,:]
    fpkms = []
    stages2 = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col="t_name")
    
    
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        stages2.append(stage)
    return fpkms, stages2

fpkms, stages= timecourse1('female')
fpkms_m, stages= timecourse1('male')

fpkms_r, stages2= timecourse2('female')
fpkms_m_r, stages2= timecourse2('male')

fig, ax = plt.subplots()
ax.plot(fpkms, "r", label= "female")
ax.plot(fpkms_m, "b", label= "male")
ax.plot([4, 5, 6, 7], fpkms_r, "r", label= "female")
ax.plot([4, 5, 6, 7], fpkms_m_r, "b", label= "male")
ax.set_title("Sxl")
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (RPKM)")
ax.set_xticklabels(stages, rotation=90)
plt.legend(bbox_to_anchor =(1.07, 0.5), loc=2, borderaxespad=0)
plt.tight_layout()
fig.savefig("replicates.png", bbox_inches='tight')
plt.close(fig)
