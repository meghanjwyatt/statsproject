#!/usr/bin/env python
import numpy
import scipy.stats

'''
Compute the correlation coefficient for the x-values in x_values and y-values
in y_values.
'''
def covariance(x, y, w):
    numpy.sum(w*(x - numpy.average(x, weights=w))*(y - numpy.average(y, weights=w))/w.sum()
              
def correlation(x, y, w):
    covariance(x,y,w)/numpy.sqrt(covariance(x,x,w)*covariance(y,y,w))
              
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
    if y_errors is None:
        r, p = scipy.stats.pearsonr(x_values, y_values)
    else:
        r = correlation(x_values, y_values, y_errors)
    msg = '''
--------------------------------------------------------------------------------
Calculation of correlation coefficient for specified x-values and specified 
y-values
--------------------------------------------------------------------------------
pearson correlation coefficient (r): {:.04e}'''.format(r)
    return
