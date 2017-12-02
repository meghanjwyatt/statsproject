#!/usr/bin/env python
import numpy

def linear(x, y, y_err):
    '''
    Perform a linear regression on the specified x values and y values,
    accounting for the specified errors y_err.

    --------
    Returns:
    --------
    m: (float) The slope of the linear fit
    b: (float) The y-intercept of the linear fit
    r: (float) The pearson correlation coefficient
    p: (float) The probability of observing a correlation coefficient at least
       as strong as that observed, given uncorrelated data.
    '''
    degree = 1
    if y_err is None:
        weights = None
    else:
        weights = 1/y_err
    (m, b), covmat = numpy.polyfit(x, y, degree, w=weights, cov=True)

    # make sure this is correct
    r = covmat[0,0]

    p = # Need to find way to calculate p

    return m, b, r, p
