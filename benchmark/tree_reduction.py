#!/usr/bin/python3

import dask.array as da

from dask.distributed import Client
from dask import delayed

import operator 

import time
import timeit

client = Client('10.255.23.115:8786')

L = range(1024)
while len(L) > 1:
  L = list(map(delayed(operator.add), L[0::2], L[1::2]))

print('I am before compute')

# Start the computation.
results = L[0].compute(scheduler='distributed')

print("Done with the compute")

L[0].visualize(filename='tree_reduction.png')
