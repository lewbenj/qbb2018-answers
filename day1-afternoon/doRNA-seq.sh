#!/bin/bash 

GENOME="../genomes/BDGP6"
DFG="../genomes/BDGP6.Ensembl.81.gtf"

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
   mkdir $SAMPLE
   fastqc ~/data/rawdata/${SAMPLE}.fastq
   hisat2 -x $GENOME -U ~/data/rawdata/${SAMPLE}.fastq -S ${SAMPLE}.sam
   samtools view -b ${SAMPLE}.sam > ${SAMPLE}.bam
   samtools sort ${SAMPLE}.bam > ${SAMPLE}/${SAMPLE}_sort.bam
   samtools index ${SAMPLE}/${SAMPLE}_sort.bam
   stringtie ${SAMPLE}/${SAMPLE}_sort.bam -p 4 -G $DFG -B -e -o ${SAMPLE}/${SAMPLE}.abund.gtf
done
