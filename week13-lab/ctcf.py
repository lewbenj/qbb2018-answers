#!/usr/bin/env python
import sys
import hifive
import numpy as np
import matplotlib.pyplot as plt
import math

"Working some magic here call me a brujo "
"Usage: ./ctcf.py"



data = hic.cis_heatmap(chrom='chr17', start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')

data[:, :, 1] *= numpy.sum(data[:, :, 0]) / numpy.sum(data[:, : 1])
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = data[:, :, 0]