#!/usr/bin/env python
import numpy
import functions.regression as regression

'''
Test the hypothesis that the correlation coefficient for the populations from 
which x_values and y_values are sampled is zero.
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
    Compute the p-value for the hypothesis that the correlation coefficient from
    which the x_values and y_values were sampled is zero.
    '''
    m, sigma_m, b, sigma_b, r, p = regression.linear(x_values, y_values, y_errors)

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
equal to zero {:s}, at the significnce level alpha = {:.04e}'''.format(p, rejection_msg, alpha)
    print(msg)
    return
