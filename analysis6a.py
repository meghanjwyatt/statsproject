#!/usr/bin/env python
import numpy
import scipy.stats

'''
Compute the correlation coefficient for the x-values in x_values and y-values
in y_values.
'''
def run(x_values, y_values):
    '''
    -----------
    Parameters:
    -----------
    x_values: (numpy.ndarray) a 1-dimensional numpy array of x-values
    y_values: (numpy.ndarray) a 1-dimensional numpy array of y-values, where
        for each i=1,2,...,n x_values[i] is paired with y_values[i].

    -----------------
    Function
    -----------------
    Compute the pearson correlation coefficient and print to stdout.
    '''
    r, p = scipy.stats.pearsonr(x_values, y_values)
    msg = '''
--------------------------------------------------------------------------------
Calculation of correlation coefficient for specified x-values and specified 
y-values
--------------------------------------------------------------------------------
pearson correlation coefficient (r): {:.04e}'''.format(r)
    return
