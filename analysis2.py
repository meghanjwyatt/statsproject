#!/usr/bin/env python
import numpy

def run(dataset1, dataset2, alpha=0.05):
    '''
    Compute the confidence limits for the difference between the samples
    dataset1 and dataset2, at the specified alpha-level.  Print the results.
    
    dataset1 and dataset2 are both numpy arrays of arbitrary size.
    '''
    
