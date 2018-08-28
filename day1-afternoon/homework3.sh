#!/bin/bash 

grep -v "^@" SRR072983.sam | grep -v 2110000 | cut -f 3 | head -n 100000 | sort | uniq -c
