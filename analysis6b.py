#!/usr/bin/env python
import numpy
import scipy.stats

'''
Compute the correlation coefficient for the x-values in x_values and y-values
in y_values.
'''
def run(x_values, y_values, alpha=0.05):
    '''
    -----------
    Parameters:
    -----------
    x_values: (numpy.ndarray) a 1-dimensional numpy array of x-values
    y_values: (numpy.ndarray) a 1-dimensional numpy array of y-values, where
        for each i=1,2,...,n x_values[i] is paired with y_values[i].
    alpha: (float) significance level for hypothesis testing

    -----------------
    Function
    -----------------
    Compute the pearson correlation coefficient and print to stdout.
    '''
    r, p = scipy.stats.pearsonr(x_values, y_values)

    if  p < alpha:
        rejection_msg = "is rejected"
    else:
        rejection_msg = "is not rejected"
    msg = '''
--------------------------------------------------------------------------------
Test of null hypothesis that correlation coefficient for specified x-values and
specified y-values is equal to zero. 
--------------------------------------------------------------------------------
p-value: {:.04e}

The null hypothesis that the correlation coefficient for the specified data is 
equal to zero {:s}, at the significnce level alpha = {.04e}'''.format(p, rejection_msg, alpha))
    print(msg)
    return
