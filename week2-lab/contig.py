#!/usr/bin/env python3
import fasta
import sys
import numpy as np

#Usage: ./contig.py <velvet_fasta_file> /<spades_fasta.fa>
#Compute the number of contigs, minimum/maximum/average contig length, and N50

# velvet_reader = fasta.FASTAReader(open(sys.argv[1]))
# spades_reader = fasta.FASTAReader(open(sys.argv[2]))



contig_compute = fasta.FASTAReader(open(sys.argv[1]))


contig_list = []


for contig_id, contig in contig_compute:
    length = len(contig)
    contig_list.append(length)
genome_length = sum(contig_list)
contig_count = len(contig_list)


print("Max = " + str(max(contig_list)))
print("Min = " + str(min(contig_list)))
print("Mean = " + str(np.mean(contig_list)))
print("Count = " + str(contig_count))


n50_list = sorted(contig_list)

mid_sum = 0
for contig in n50_list:
    mid_sum += contig
    if mid_sum > (genome_length/2):
        print("N50 = " + str(contig))
        break
 