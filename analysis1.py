#!/usr/bin/env python
import numpy
import scipy.stats
import matplotlib.pyplot as pyplot

'''
Generate a quantile-quantile plot, given an array of data.
'''

def run(dataset):
    '''
    -----------
    Parameters:
    -----------
    dataset: (numpy.ndarray) a 1-dimensional numpy array of data.

    -----------------
    Function
    -----------------
    Displays Q-Q plot, comparing normalized data to N(0,1) distribution
     
    '''
    # sample mean
    mean = dataset.mean()
    # square root of sample variance
    stdev = numpy.sqrt(dataset.var(ddof=1))

    normalized_dataset = (dataset - mean)/stdev
    normalized_dataset.sort()

    n = normalized_dataset.shape[0]
    quantiles = (numpy.arange(1, n+1, dtype=float)-0.5)/n
    
    theoretical_values = scipy.stats.norm.ppf(quantiles)

    pyplot.plot(normalized_dataset, theoretical_values, 'o', color='black')

    pyplot.xlabel("Input data (normalized)")
    pyplot.ylabel("Normal distribution")

    xmin = min(normalized_values.min(), theoretical_values.min())
    xmax = max(normalized_values.max(), theoretical_values.max())

    # Plot a diagonal line
    pyplot.plot((xmin, xmax) (xmin, xmax), color='black')

    pyplot.show()
    return
