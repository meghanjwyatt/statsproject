#!/usr/bin/env python
import numpy
import scipy.stats
import matplotlib.pyplot as pyplot

'''
Generate a quantile-quantile plot, given an array of data.
'''

def run(dataset):
    '''
    -----------
    Parameters:
    -----------
    dataset: (numpy.ndarray) a 1-dimensional numpy array of data.

    -----------------
    Function
    -----------------
    Displays Q-Q plot, comparing normalized data to N(0,1) distribution
     
    '''
    #Calculate quantile values
    scipy.stats.probplot(dataset, plot=pyplot)
    #Display plot
    pyplot.show()
    return
