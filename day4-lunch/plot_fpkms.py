#!/usr/bin/env python3
import sys 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#Usage: ./plot_fpkms.py ~/data/results/stringtie/SRR072893/t_data.ctab ~/data/results/stringtie/SRR072915/t_data.ctab 
#create scatter plot of log FPKM values of two samples

fpkm1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name").loc[:, "FPKM"]
fpkm2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name").loc[:, "FPKM"]

fit = np.polyfit(fpkm1, fpkm2, 1)
p = np.poly1d(fit)
xplin = np.linspace(0,fpkm1.max())

fig, ax = plt.subplots()
ax.scatter(fpkm1, fpkm2, alpha = 0.5)
# ax.set_xscale('log')
# ax.set_yscale('log')
plt.plot(xplin, p(xplin))
plt.yscale("log")
plt.xscale("log")
plt.axis([0.001, 10000, 0.001,10000])
axes = plt.gca()
ax.set_xlabel("logFPKM1")
ax.set_ylabel(" logFPKM2")
fig.suptitle("FPKM1 vs FPKM2")
fig.savefig( "name.png")
ax.set_xlim
#coeff = np.polyfit(fpkm1_log, fpkm2_log, 1)
#np.poly1d()
#x = linspace() 
 
plt.close(fig)



#numpy.polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)[source]

#best_fit = np.p