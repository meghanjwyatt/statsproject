#!/usr/bin/env python
import numpy
import scipy.stats

'''
Compute the probability that an uncorrelated distribution of x/y values produces
the correlation at least as extreme as that observed with the data.
'''
def run(x_values, y_values, y_errors, alpha=0.05):
    '''
    -----------
    Parameters:
    -----------
    x_values: (numpy.ndarray) a 1-dimensional numpy array of x-values
    y_values: (numpy.ndarray) a 1-dimensional numpy array of y-values, where
        for each i=1,2,...,n x_values[i] is paired with y_values[i].
    y_errors: (numpy.ndarray or None) the errors associated with each value
    alpha: (float) significance level for hypothesis testing

    -----------------
    Function
    -----------------
    Compute the pearson correlation coefficient and print to stdout.
    '''
    
