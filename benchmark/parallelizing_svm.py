#!/usr/bin/python3
import pandas as pd
import seaborn as sns
import sklearn.datasets
from sklearn.svm import SVC

import dask_ml.datasets
from dask_ml.wrappers import ParallelPostFit

import dask.array as da

from dask.distributed import Client
from dask import delayed

import operator 

import time
import timeit

client = Client('10.255.23.115:8786')

print('I am before compute')


# Start the computation.


X, y = sklearn.datasets.make_classification(n_samples=1000)
clf = ParallelPostFit(SVC(gamma='scale'))
clf.fit(X, y)

X, y = dask_ml.datasets.make_classification(n_samples=800000,
                                            random_state=800000,
                                            chunks=800000 // 20)

# Start the computation.
results = clf.predict(X).compute(scheduler='distributed')


print("Done with the compute")

clf.predict(X).visualize(filename='parallel_svm.png')
