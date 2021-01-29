#!/usr/bin/python3

import dask.array as da

from dask.distributed import Client
from dask import delayed

import time
import timeit

client = Client('10.255.23.115:8786')


# Compute the SVD of 'Tall-and-Skinny' Matrix 
X = da.random.random((10000, 10000), chunks=(2000, 2000))
u, s, v = da.linalg.svd_compressed(X, k=5)

print('I am before compute')

# Start the computation.
results = v.compute(scheduler='distributed')

print('I am done with the compute')


v.visualize(filename='svd_square_matrix.svg')

