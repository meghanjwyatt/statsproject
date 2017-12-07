#!/usr/bin/env python
import numpy
import scipy.stats

def covariance(x, y, w):
    return numpy.sum(w*(x - numpy.average(x, weights=w))*(y - numpy.average(y, weights=w)))/w.sum()
              
def correlation(x, y, w):
    return covariance(x,y,w)/numpy.sqrt(covariance(x,x,w)*covariance(y,y,w))

def linear(x, y, y_err):
    '''
    Perform a linear regression on the specified x values and y values,
    accounting for the specified errors y_err.

    --------
    Returns:
    --------
    m: (float) The slope of the linear fit
    sigma_m: (float) The error in the slope of the linear fit
    b: (float) The y-intercept of the linear fit
    sigma_b: (float) The error in the y-intercept of the linear fit
    r: (float) The pearson correlation coefficient
    p: (float) The probability of observing a correlation coefficient at least
       as strong as that observed, given uncorrelated data.
    '''
    n = len(x)
    degree = 1
    if y_err is None:
        weights = None
    else:
        weights = 1/y_err
    m, b = numpy.polyfit(x, y, degree, w=weights)

    # Calculate correlation coefficient and p-value
    if weights is None:
        r,p = scipy.stats.pearsonr(x,y)  
    else:
        r = correlation(x,y,weights)
        t = r*numpy.sqrt(n-2)/numpy.sqrt(1-r**2)
        t = abs(t)

        p = 2*(1-scipy.stats.t.cdf(t,n-2,0,1))
        
    #Calculate uncertainties in slope and intercept
    y_fit =m*x+b
    mse = numpy.sum((y-y_fit)**2)/(n-2)
    
    var_m = mse/(numpy.sum(x**2)-(numpy.sum(x))**2/n)
    sigma_m = numpy.sqrt(var_m)
    
    var_b = mse*(1./n+x.mean()**2/numpy.sum((x-x.mean())**2))
    sigma_b = numpy.sqrt(var_b)
    
    return m, sigma_m, b, sigma_b, r, p
