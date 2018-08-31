#!/usr/bin/env python3
import sys 
import pandas as pd
import os 
import matplotlib.pyplot as plt 
import numpy as np
#usage: ./ma_plot.py <ctab_file>

df1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
df2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm1 = df1.loc[:, "FPKM"]
fpkm2 = df2.loc[:, "FPKM"]

ratio = np.log2(fpkm1 + 1) - np.log2(fpkm2 + 1)
avg = 0.5*(np.log2(fpkm1 + 1) + np.log2(fpkm2 + 1))

fig, ax = plt.subplots()
ax.scatter(avg, ratio, alpha= 0.5)
ax.set_xlabel("Average")
ax.set_ylabel("Ratio")
ax.set_title("MA-plot")
fig.savefig("maplot.png")
plt.close(fig)
# fpkm1_log = np.log(fpkm1 + 1)
# fpkm2_log = np.log(fpkm2 + 1)
