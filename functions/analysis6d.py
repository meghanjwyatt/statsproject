#!/usr/bin/env python
import numpy
import scipy.stats

'''
Perform a linear regression.
'''
def run(x_values, y_values, y_errors):
    '''
    -----------
    Parameters:
    -----------
    x_values: (numpy.ndarray) a 1-dimensional numpy array of x-values
    y_values: (numpy.ndarray) a 1-dimensional numpy array of y-values, where
        for each i=1,2,...,n x_values[i] is paired with y_values[i].
    y_errors: (numpy.ndarray or None) the errors associated with each value

    -----------------
    Function
    -----------------
    Perform a linear regression and show the resulting plot.
    '''
    
