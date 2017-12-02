#!/usr/bin/env python
import numpy
import scipy.stats

'''
Test the null hypothesis that the mean of dataset1 is equal to the mean of 
dataset2. Homoscedastic (equal variance) test.
'''
def run(dataset1, dataset2, tails, alpha=0.05):
    '''
    -----------
    Parameters:
    -----------
    dataset1: (numpy.ndarray) a 1-dimensional numpy array of data; arbitrary 
        length; the first of the samples to be compared
    dataset2: (numpy.ndarray) a 1-dimensional numpy array of data; arbitrary 
        length; the second of the samples to be compared
    tails: (int) the number of tails for the data set
    alpha: signficance level for rejecting the null hypothesis that the means of
        the populations from which samples dataset1 and dataset2 are drawn are 
        equal.

    -----------------
    Function
    -----------------
    Print to standard out the probability of observing a sample with mean at 
    least as distant from the sample mean of dataset1 as the sample mean of 
    dataset2, assuming that the samples are Student t distributed (small sample;
    n < 30) or z distributed (large sample, n > 30), with variance estimated
    from the sample variances of dataset1 and dataset2.
    '''
    # small sample
    if n < 30:
        t_statistic, p_value = scipy.stats.ttest_ind(dataset1, dataset2)
    # large sample
    else:
        n1 = dataset1.shape[0]
        n2 = dataset2.shape[0]
        effective_n = numpy.sqrt(n1*n1/(n1+n2)) # need to check
        sigma = #??? 
        difference = abs(dataset1.mean() - dataset2.mean())
        p = 2*scipy.stats.norm.cdf(-difference, loc=0, scale=sigma)

    # account for one-tailed vs two-tailed tests
    p_value /= tails

    if p_value < alpha:
        rejection_msg = "is rejected"
    else:
        rejection_msg = "is not rejected"
    msg = '''
--------------------------------------------------------------------------------
Test of null hypothesis that the means of the specified samples are equal via a
homoscedastic t test or z test.
--------------------------------------------------------------------------------
p-value: {:.04e}

The null hypothesis that the means of the populations from which the specified 
samples where drawn are the same {:s}, at the alpha={.04e} level.
'''.format(p_value, rejection_msg, alpha)
    print(msg)
