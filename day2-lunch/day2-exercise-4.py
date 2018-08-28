#!/usr/bin/env python3
import sys 

if len(sys.argv) > 1:
    f = open( sys.argv[1])
else:
    f = sys.stdin

outcome = []
for line in f:
    if line.startswith("@"):
        continue
        count += 1
    data = line.rstrip("r\n").split("\t")
    outcome.append(data[2])
     
 
    if len(outcome) >= 10:
        print(outcome)
        break 
