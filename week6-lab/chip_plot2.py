#!/usr/bin/env python3

import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import math

"Usage: Produce a two panel plot containing two bar plots."
#././chip_plot2.py gained_peaks.bed lost_peaks.bed ER4_all.bed G1E_all.bed

for line in open(sys.argv[1]):
    num_lines_gained = sum(1 for line in open(sys.argv[1]))
    print(num_lines_gained)

    num_lines_lost = sum(1 for line in open(sys.argv[2]))
    print(num_lines_lost)

    ER4_all = sum(1 for line in open(sys.argv[3]))
    print(ER4_exons)

    G1E_all = sum(1 for line in open(sys.argv[4]))
    print(G1E_exons)


fig, ax = plt.subplots(ncols = 2, figsize = (25,10))

ax[1].bar(x = 0, height = 130, label = "Sites Gained", color = "skyblue")
ax[1].bar(x = 1, height = 54, label = "Sites Lost", color = "gray")
ax[1].legend()
ax[1].set_title("Site Differences After G1E to ER4 Transition")
ax[1].set_xticks([])
ax[1].set_ylabel("Counts")

ax[0].bar(x = 0, height = 507, label = "ER4 Exons", color = "orchid")
ax[0].bar(x = 1, height = 457, label = "G1E Exons", color = "purple")
ax[0].bar(x = 2, height = 321, label = "ER4 Introns", color = "olive")
ax[0].bar(x = 3, height = 286, label = "G1E Introns", color = "darkgreen")
ax[0].bar(x = 4, height = 566, label = "ER4 Promoters", color = "coral")
ax[0].bar(x = 5, height = 509, label = "G1E Promoters", color = "sienna")
ax[0].legend()
ax[0].set_title("CTCF Site Types in G1E and ER4")
ax[0].set_xticks([])
ax[0].set_ylabel("Counts")

fig.savefig("chip_plot.png")
plt.close(fig)