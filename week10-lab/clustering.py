#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list 
from scipy.spatial.distance import pdist

"Usage: perform heiracrchical clustering"
# ./clustering.py hema_data1.txt

data = []
 
for line in open(sys.argv[1]):
    fields = line.rstrip("r\n").split()
    cfu = fields[1]
    poly = fields[2]
    data.append([cfu, poly])
#print(data)
z = ward(pdist(data))
#print(z)
y = leaves_list(z)
#print(y)
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(z)
fig.savefig("dendrogram.png")
plt.close(fig)


    
