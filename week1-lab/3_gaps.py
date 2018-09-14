#!/usr/bin/env python3
import fasta
import sys
#from itertools import zip

#Usage: 01-week1.py <dna_file> <aa file> : ./3_gaps.py week1_blast_output.fa align_aa_seq.out
#Iterating nucleotide alignment over protein alignment. Three gaps to be inserted wherever there is a gap in the protein alignment.


dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))
n_seq = []
for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
    new_dna = []
    j =0
    for i in range(len(aa)):
        a = aa[i]
        n = dna[j: j + 3]
        
        if a == '-':
                n = "---"
                new_dna.append(n)
        else:
            j+=3
            new_dna.append(n)
        
    n_seq.append(new_dna)
    
print(n_seq)