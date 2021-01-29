#!/usr/bin/python3

import dask.array as da

from dask.distributed import Client
from dask import delayed

import time
import timeit

client = Client('10.255.23.115:8786')

# Compute the SVD of 'Tall-and-Skinny' Matrix
X = da.random.random((200000, 1000), chunks=(10000, 1000))
u, s, v = da.linalg.svd(X)

# Start the computation.
results = v.compute(scheduler='distributed')

v.visualize()



