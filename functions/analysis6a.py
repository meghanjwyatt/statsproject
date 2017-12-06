#!/usr/bin/env python
import numpy
import scipy.stats
import regression

'''
Compute the correlation coefficient for the x-values in x_values and y-values
in y_values.
'''

def run(x_values, y_values, y_errors):
    '''
    -----------
    Parameters:
    -----------
    x_values: (numpy.ndarray) a 1-dimensional numpy array of x-values
    y_values: (numpy.ndarray) a 1-dimensional numpy array of y-values, where
        for each i=1,2,...,n x_values[i] is paired with y_values[i].
    y_errors: (numpy.ndarray or None) the uncertainties (standard deviation) associated with each value
    -----------------
    Function
    -----------------
    Compute the pearson correlation coefficient and print to stdout.
    '''
    m, sigma_m, b, sigma_b, r, p = regression.linear(x_values, y_values, y_errors)
    
    msg = '''
--------------------------------------------------------------------------------
Calculation of correlation coefficient for specified x-values and specified 
y-values
--------------------------------------------------------------------------------
pearson correlation coefficient (r): {:.04e}'''.format(r)
    print(msg)
    return
