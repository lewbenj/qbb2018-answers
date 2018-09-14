#!/usr/bin/env python3
import fasta
import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests
#from itertools import zip

#Usage: 01-week1.py <dna_file> <aa file> : ./mut.py week1_blast_output.fa align_aa_seq.out
#Iterating nucleotide alignment over protein alignment. Three gaps to be inserted wherever there is a gap in the protein alignment.


dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))
n_seq = []
all_aa_seq=[]
for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
    new_dna = []
    new_aa=[]
    j =0
    for i in range(len(aa)):
        a = aa[i]
        n = dna[j: j + 3]
        
        if a == '-':
                n = "---"
                new_dna.append(n)
                new_aa.append(a)
        else:
            j+=3
            new_dna.append(n)
            new_aa.append(a)
        
    n_seq.append(new_dna)
    
#print(n_seq)
    all_aa_seq.append(new_aa)

amino_list = all_aa_seq[0]
dna_list = n_seq[0]

dN = [0] * len(amino_list)
dS = [0] * len(dna_list)


for i in range(1, len(all_aa_seq[1:])):
    list_align = all_aa_seq[i]
    
    for j in range(len(list_align)):
        if list_align[j] != amino_list[j]:
            dN[j] += 1
        else:
            dS[j] += 1
			
# print(dN)
# print(dS)
ratio_list = []
for i in range(len(dS)):
    dSN = dN[i] / (dS[i] + 1)
    ratio_list.append(dSN)

#print(ratio_list)
# what the hell am I doing?

ztest = stests.ztest(dN, dS)
print(ztest)

fig, ax = plt.subplots()
plt.scatter(range(0, len(ratio_list)), ratio_list, alpha = 0.5, s = 3, color ='blue')
ax.set_ylabel("Ratio of dN/dS")
ax.set_xlabel("Amino Acid Postion")
ax.set_title("Ratio of dS/dn vs Amino Acid Position")
plt.tight_layout()
fig.savefig("dN/dS.png")
plt.close(fig)