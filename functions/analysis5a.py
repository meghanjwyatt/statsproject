#!/usr/bin/env python
import numpy
import scipy.stats

'''
Test the null hypothesis that the mean of a dataset is equal to a specified
value.
'''
def run(dataset, hypothesized_mean, tails, p=0.05):
    '''
    -----------
    Parameters:
    -----------
    dataset: (numpy.ndarray) a 1-dimensional numpy array of data; arbitrary 
        length
    hypothesized_mean: (float) the mean of the data set under the null
        hypothesis
    tails: (int) the number of tails for the data set

    -----------------
    Function
    -----------------
    Print to standard out the probability of observing a data set with mean at 
    least as different from the hypothesized mean as the mean observed in 
    data set, given that data set is t-distributed (small dat aset; n < 30) or 
    z-distributed (large data set; n >= 30).
    '''
    # First, check that tails makes sense:
    if not tails in (1,2):
        raise ValueError("tails must be 1 or 2, but the value {:s} was "
                         "specified. Exiting...".format(str(tails)))
    n = len(dataset)
    mean = dataset.mean()
    stdev = numpy.sqrt(dataset.var(ddof=1))

    # small data set
    if n < 30:
        if mean >= hypothesized_mean:
            raw_p = 1-scipy.stats.t.cdf(mean, 
                                        n-1, # degrees of freedom
                                        loc=hypothesized_mean,
                                        shape=stdev)
        else:
            raw_p = scipy.stats.t.cdf(mean, 
                                      n-1, # degrees of freedom
                                      loc=hypothesized_mean,
                                      shape=stdev)

    # large data set; n >= 30
    else:
        if mean >= hypothesized_mean:
            raw_p = 1-scipy.stats.norm.cdf(mean,
                                           loc=hypothesized_mean,
                                           shape=stdev/numpy.sqrt(n))
        else:
            raw_p = scipy.stats.norm.cdf(mean,
                                         loc=hypothesized_mean,
                                         shape=stdev/numpy.sqrt(n))
    p = raw_p * tails

    if p < alpha:
        significance_msg = "is rejected"
    else:
        significance_msg = "is not rejected"

    msg = '''
--------------------------------------------------------------------------------
Test of null hypothesis that the mean of the population from which the specified
sample was drawn is equal to {:.04e}.
--------------------------------------------------------------------------------
sample mean: {:.04e}
mean under null hypothesis: {:.04e}
tails: {:d}

p-value: {:.04e}

The null hypothesis {:s}, at the specified alpha-level p = {:.04e}.
'''.format(hypothesized_mean, mean, hypothesized mean, tails, p, 
           significance_msg, alpha)
    print(msg)
    return
