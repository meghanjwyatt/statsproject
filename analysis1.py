#!/usr/bin/env python
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
    
    pass
