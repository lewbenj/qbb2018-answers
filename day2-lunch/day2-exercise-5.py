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
    data = line.rstrip("\r\n").split("\t")
    outcome.append(int(data[4]))

print(sum(outcome)/ len(outcome))
