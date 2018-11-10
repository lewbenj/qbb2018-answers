#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns
import pandas as pd

"usage: "
#heatmap.py hema_text.txt

d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)
cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)

ax = sns.clustermap(df, cmap=cmap)
plt.show()
ax.savefig("heatmap.png")
plt.close(ax)