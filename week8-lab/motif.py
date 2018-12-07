#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

"Usage: Produce a plot showing where motif matches occur in the input sequence"
#./motif.py <meme.txt>

for line in open(sys.argv[1]):
    