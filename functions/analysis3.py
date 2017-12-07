#!/usr/bin/env python
import numpy
import scipy.stats

def run(dataset1, dataset2, alpha=0.05):
    '''
    -----------
    Parameters:
    -----------
    dataset1: (numpy.ndarray) a 1-dimensional numpy array of data; arbitrary 
        length
    dataset2: (numpy.ndarray) a 1-dimensional numpy array of data; arbitrary
        length

    -----------------
    Function
    -----------------
    Prints to stdout the confidence limits for the difference between the
    samples dataset1 and dataset2, at the specified alpha level.
    '''
     
    n1 = len(dataset1)
    n2 = len(dataset2)
    mean1 = dataset1.mean()
    mean2 = dataset2.mean()
    var1 = dataset1.var(ddof=1)
    var2 = dataset2.var(ddof=1)
    dmean = mean1 - mean2

    # Large sample size; n1 >= 30 AND n2 >=30
    if n1 >= 30 and n2 >= 30:
        
        zmin, zmax = scipy.stats.norm.interval(1-alpha, 
                                               loc=0, 
                                               scale=1)
        upperlimit = dmean + zmax*numpy.sqrt(var1/numpy.sqrt(n1)+var2/numpy.sqrt(n2))
        lowerlimit = dmean + zmin*numpy.sqrt(var1/numpy.sqrt(n1)+var2/numpy.sqrt(n2))
        

    # Small sample size; n1 or n2 < 30
    else:
        dof = int(((var1/n1+var2/n2)**2)/(((var1/n1)**2)/(n1-1)+((var2/n2)**2)/(n2-1)))
        tmin, tmax = scipy.stats.t.interval(1-alpha,
                                            dof,
                                            loc=0,
                                            scale = 1)
        upperlimit = mean + tmax*numpy.sqrt(var1/numpy.sqrt(n1)+var2/numpy.sqrt(n2))
        lowerlimit = mean + tmin*numpy.sqrt(var1/numpy.sqrt(n1)+var2/numpy.sqrt(n2))

    msg = '''
-------------------------------------------
Confidence limits for mean of input dataset
-------------------------------------------
{:.02f}% confidence interval:
    mean of dataset 1:           {:.04e}
    mean of dataset 2:           {:.04e}
    difference between means:    {:.04e}
    lower limit:                 {:.04e}
    upper limit:                 {:.04e}
    '''.format((1-alpha)*100, mean1, mean2, dmean, lowerlimit, upperlimit)
    print(msg)
    return
