#!/usr/bin/python3

import dask.array as da

from dask.distributed import Client
from dask import delayed

import time
import timeit

name = 'svd_tall_skinny_matrix_1M_x_2k'

client = Client('10.255.23.115:8786', name = name)


# Compute the SVD of 'Tall-and-Skinny' Matrix
X = da.random.random((1000000, 2000), chunks=(10000, 2000))
u, s, v = da.linalg.svd(X)

# Start the computation.
results = v.compute(scheduler='distributed')

v.visualize(filename=f'{name}.png')



