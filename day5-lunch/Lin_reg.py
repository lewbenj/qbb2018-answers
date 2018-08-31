#!/usr/bin/env python3
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Usage:./Lin_reg.py <orig_ctab_file>
# ./Lin_reg.py ~/qbb2018-answers/day5-lunch/H3K4me1.tab ~/qbb2018-answers/day5-lunch/H3K4me3.tab ~/qbb2018-answers/day5-lunch/H3K9ac.tab ~/qbb2018-answers/day5-lunch/H3K27ac.tab ~/qbb2018-answers/day5-lunch/H3K27me3.tab ~/data/results/stringtie/SRR072893/t_data.ctab 

#Perform ordinary linear regression for all of the four marks to determine how predictive each is of gene expression
# X = [] avg histone means
# Y = [] fpkms from ctab_file

# threshold = int(sys.argv[1])
# ctab_variable = len(sys.argv)
# d_fpkm = {}
#
# for i in range(1,(ctab_variable)):
histone_mean = {}
histone_1 = sys.argv[1].split(os.sep)[-1]
mean1 = pd.read_csv(sys.argv[1], sep = "\t", index_col=0).iloc[:, 4]

histone_2 = sys.argv[2].split(os.sep)[-1]
mean2 = pd.read_csv(sys.argv[2], sep = "\t", index_col=0).iloc[:, 4]

histone_3 = sys.argv[3].split(os.sep)[-1]
mean3 = pd.read_csv(sys.argv[3], sep = "\t", index_col=0).iloc[:, 4]

histone_4 = sys.argv[4].split(os.sep)[-1]
mean4 = pd.read_csv(sys.argv[4], sep = "\t", index_col=0).iloc[:, 4]

histone_5 = sys.argv[5].split(os.sep)[-1]
mean5 = pd.read_csv(sys.argv[5], sep = "\t", index_col=0).iloc[:, 4]

fpkms = sys.argv[6].split(os.sep)[-1]
fpkm_transcript = pd.read_csv(sys.argv[6], sep = "\t", index_col="t_name").loc[:, "FPKM"]


histone_mean = {histone_1: mean1, histone_2: mean2, histone_3: mean3, histone_4: mean4, histone_5: mean5, fpkms: fpkm_transcript}
histone_mean_df = pd.DataFrame(histone_mean)
#print(histone_mean_df)
histone_mean_df = histone_mean_df.dropna()

y = histone_mean_df.loc[:,fpkms]
x = histone_mean_df.loc[:,[histone_1,histone_2,histone_3,histone_4,histone_5,]]
model = sm.OLS(y, x)
# model = sm.OLS(y, X)
# print(model)
results = model.fit()
print(results.summary())


