#!/usr/bin/env python
import numpy
import scipy.stats

'''
Test the null hypothesis that the proportion of samples in corresponding 
categories of each data set are equal.
'''
def run(*datasets, alpha=0.05):
    '''
    -----------
    Parameters:
    -----------
    *datasets: (numpy.ndarray) 1-dimensional numpy arrays of data; arbitrary 
        length; the samples to be compared, which should be integer-valued 
        categorical data
    alpha: signficance level for rejecting the null hypothesis that the means of
        the populations from which samples dataset1 and dataset2 are drawn are 
        equal.

    -----------------
    Function
    -----------------
    '''
    # small sample
    if n < 30:
    # large sample
    else:

    # account for one-tailed vs two-tailed tests
    p_value /= tails

    if p_value < alpha:
        rejection_msg = "is rejected"
    else:
        rejection_msg = "is not rejected"
    msg = '''
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
p-value: {:.04e}

'''.format()
    print(msg)
