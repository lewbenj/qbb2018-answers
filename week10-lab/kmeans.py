#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list, fcluster
from scipy.spatial.distance import pdist

"usage: "
#kmeans.py hema_text.txt

import numpy as np
from sklearn.cluster import KMeans

d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)


kmeans = KMeans(n_clusters=7)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)

plt.figure()
plt.title("Kmeans Plot")
plt.scatter(df["CFU"], df['poly'], c=y_kmeans, s=5, cmap='viridis')
plt.ylabel("Poly expression")
plt.xlabel("CFU expression")
plt.savefig("kmeans.png")
plt.close()