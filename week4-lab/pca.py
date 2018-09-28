#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

#Usage : plot first two components to visualize genetic relatedness between genetic screens
# ./pca.py plink.eigenvec 
x_1 = []
y_1 = []

for line in open(sys.argv[1]):
    fields = line.split(" ")
    x = fields[2]
    y = fields[3]
    x_1.append(float(x))
    y_1.append(float(y))
   # print(x_1)

fig, ax = plt.subplots()
plt.scatter(x_1, y_1)
plt.ylabel("Genetic Relatedness ")
plt.xlabel("Strains")
ax.set_title("PCA")
plt.tight_layout
fig.savefig("pca.png") 
plt.close(fig)

