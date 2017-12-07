#!/usr/bin/env python
import numpy
import scipy.stats

'''
Test the null hypothesis that the proportion of samples in corresponding 
categories of each data set are equal.
'''
def run(datasets, alpha=0.05):
    '''
    -----------
    Parameters:
    -----------
    datasets: (list of numpy.ndarray) 1-dimensional numpy arrays of data; 
        arbitrary length; the samples to be compared, which should be 
        integer-valued categorical data.
    alpha: signficance level for rejecting the null hypothesis that the means of
        the populations from which samples dataset1 and dataset2 are drawn are 
        equal.

    -----------------
    Function
    -----------------
    '''
    print(numpy.array(datasets))
    chi2, p, _, _ = scipy.stats.chi2_contingency(numpy.array(datasets))

    if p < alpha:
        rejection_msg = "is rejected"
    else:
        rejection_msg = "is not rejected"
    msg = '''
--------------------------------------------------------------------------------
Chi-squared Contingency Test for Relationship Between Rows and Columns
--------------------------------------------------------------------------------
chi-squared statistic: {:.04e}
p-value: {:.04e}

The null hypothesis that there is no relationship between rows and columns
{:s} at the alpha-level of {:.04e}.

'''.format(chi2,p,rejection_msg,alpha)
    print(msg)
