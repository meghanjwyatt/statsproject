#!/usr/bin/env python
import numpy
import scipy.stats

'''
Compute mean confidence limits based on student t or z distribution
'''
def run(dataset, alpha=0.05):
    '''
    -----------
    Parameters:
    -----------
    dataset: (numpy.ndarray) a 1-dimensional numpy array of data; arbitrary 
        length

    -----------------
    Function
    -----------------
    Prints to stdout the confidence limits for the mean of dataset, at the 
    specified alpha level.
    '''
    n = len(dataset)
    mean = dataset.mean()
    stdev = numpy.sqrt(dataset.var(ddof=1))

    # Large sample size; n >= 30
    if n >= 30:
        
        zmin, zmax = scipy.stats.norm.interval(1-alpha, 
                                               loc=0, 
                                               scale=1)
        upperlimit = mean + zmax*stdev/numpy.sqrt(n)
        lowerlimit = mean + zmin*stdev/numpy.sqrt(n)
        

    # Small sample size; n < 30
    else:
        # Need to check
        xmin, xmax = scipy.stats.t.interval(1-alpha,
                                            n-1, # degrees of freedom
                                            loc=mean,
                                            scale = stdev

    msg = '''
-------------------------------------------
Confidence limits for mean of input dataset
-------------------------------------------
{:.02f}% confidence interval:
    mean:    {:.04e}
    lower limit: {:.04e}
    upper limit: {:.04e}
    '''.format((1-alpha)*100, mean, lowerlimit, upperlimit)
    print(msg)
    return
