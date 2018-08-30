#!/usr/bin/env python3
import sys 
import fasta

#create kmer matcher
#./kmer_matcher.py < subset.fa droYak2_seq.fa <k>, where k is ajhv



target = fasta.FASTAReader(open(sys.argv[1]))
query = fasta.FASTAReader(open(sys.argv[2]))
#reader = fasta.FASTAReader(query)
k = int(sys.argv[3])

query_kmers = {}

for ident, sequence in query:
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in query_kmers:
            query_kmers[kmer] = [i]
        else:
            query_kmers[kmer].append(i) # adds position to the kmers
        #print(query_kmers) #to test dictionary
for ident, sequence in target:
    for i in range(0, len(sequence) - k):
        target_kmer = sequence[i:i+k]
        if target_kmer in query_kmers:
            print(ident, i, query_kmers[target_kmer], target_kmer)


#for key in query_kmers:
     #print(key, query_kmers[key])
     
     
     
     
     
