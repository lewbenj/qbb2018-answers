#!/usr/bin/env python3
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Usage: ./random_gene.py <samples.csv> <ctab_file> <gene_name> ....
# Random gene 


fpkms = []

df = pd.read_csv(sys.argv[1])

for i in range(0, len(sys.argv)): 
    compiled = {}
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        df = pd.read_csv(sys.argv[1])

        roi = ctab_df.loc[:, "gene_name"] == sys.argv[i]
        compiled = ctab_df.loc[roi, "FPKM"]
        dfcompiled = pd.DataFrame(compiled)
    ##transcrip vs FPKMS avg of FPKMS
        average = dfcompiled.mean(axis = 1)

        #print(average)

        fig, ax = plt.subplots()
        ax.plot(list(dfcompiled.index), list(average), alpha = 0.75, color = "red")
        #ax.plot(list(males), males.loc[transcript_id,:], color = "blue")
        ax.set_title(sys.argv[i])
        #plt.xlabel("developmental stage", fontsize = :sunglasses:
        #plt.ylabel("mRNA Abundance (FPKM)", fontsize = :sunglasses:
        #plt.legend(bbox_to_anchor = (1.05, 0.5), loc = 2, borderaxespad = 0., labels = ["Female", "Male"])
        plt.xticks(rotation=90)
        plt.tight_layout()
        fig.savefig("variable.png")
        plt.close(fig)