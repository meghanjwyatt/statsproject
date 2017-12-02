#!/usr/bin/env python
import numpy

def run(dataset1, dataset2, alpha=0.05):
    '''
    -----------
    Parameters:
    -----------
    dataset1: (numpy.ndarray) a 1-dimensional numpy array of data.
    dataset2: (numpy.ndarray) a 1-dimensional numpy array of data.

    -----------------
    Function
    -----------------
    Prints to stdout the confidence limits for the difference between the
    samples dataset1 and dataset2, at the specified alpha level.
    '''
    
