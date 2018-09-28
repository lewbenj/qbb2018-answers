#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
 
 # Usage: create a histogram to visualize allele frequencies
 # ./allele_freq.py BYxRM_segs_saccer3.bam.simplified.vcf

# anno = open(sys.argv[1])
all_freq = []

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
        
    else: 
        fields = line.rstrip("\rn").split("\t")
        frequency = fields[7]
        allele = frequency.split("=")[1]
        allele_want = allele.split(",")[0]
        all_freq.append(float(allele_want))
                
                    
fig, ax = plt.subplots()
plt.hist(all_freq, bins = 1000)
plt.xlabel("Allele")
plt.ylabel("Frequency")
ax.set_title("Spectrum")
plt.tight_layout
fig.savefig("allele_fre.png")
plt.close(fig)


                    
