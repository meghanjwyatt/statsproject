#!/usr/bin/env python
import datainput
import analysis1


class StatsTool(object):
    def __init__(self):
        self.get_analysis_type()
        self.run()
        
    def get_analysis_type(self):
        '''
        Prompt the user with analysis options. Set the attribute
        ``self.analysistype`` to the number or number/letter combination
        specified by the user.
        '''
        
        msg = \
'''
-----------------------------
statstool.py

By Meghan Wyatt and David Lee
-----------------------------

Analysis options:
1) Plot a Q-Q plot for a set of x/y data
2) Compute mean confidence limits
3) Compute confidences limits for the difference between samples
4) Compute mean confidence limits for a sample via bootstrapping
5a) Tests for population mean
5b) Tests for difference between means of two populations
5c) Chi-Squared test
6a) Compute correlation coefficient ("r") for a set of x/y data
6b) Carry out hypothesis testing on the correlation coefficient
6d) Perform a linear regression on a set of x/y data
7) Propagation of error
-----------------------------

'''
        print(msg)
        self.analysistype = input("Please input the number (or number/letter "
                                  "combination) of the desired analysis.")
                                  
    def run(self):
        if self.analysistype == '1':
            dataset1, dataset2 = datainput.input1()
            analysis1.run(dataset1, dataset2)
            
        if self.analysistype == '2':
            'continue here'
            
        

