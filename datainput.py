#!/usr/bin/env python
import numpy

class DataInput(object):
    '''
    Framework for loading user-specified data. Enables input of data via files
    or via ``manual`` user input. 
    
    Types of data that may need to be loaded:
    
    One data set of arbitrary size:
        2) mean confidence limits
        4) confidence limits for a sample using simulation
        5a) Large and small sample tests for population mean
        
    Two data sets of arbitrary sizes:
        3) Confidence limits for the difference between samples
        5b) Large and small sample tests for the difference between two means
    
    Two data sets of same size:
        1) Q-Q plot for a set of x/y data (???)
        5c) Chi-squared test
        6a) Correlation coefficient of x/y data
        6b) Carry out hypothesis testing on the correlation coefficient (H0 = (r = 0))
        6d) Perform linear regression on a set of x/y data
        
    Also, we need data input for propagation of error calculations (7), and we need to 
    allow input of single values, for use with (5a) large and small sample tests for 
    population mean.
        
    '''
    def __init__(self):
        pass
        
    def load_from_file(self, filepath):
        data = numpy.loadtxt(filepath)
