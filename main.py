#!/usr/bin/env python
import datainput
import analysis1
import analysis4


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
                                  "combination) of the desired analysis, and then "
                                  "press Enter.\n")
                                  
    def run(self):
        if self.analysistype == '1':
            dataset1, dataset2 = datainput.input1()
            analysis1.run(dataset1, dataset2)
            
        elif self.analysistype == '2':
            dataset = datainput.input2()
            analysis2.run(dataset)
            
        elif self.analysistype == '3':
            dataset1, dataset2 = datainput.input3()
            analysis3.run(dataset1, dataset2)
            
        elif self.analysistype == '4':
            dataset = datainput.input4()
            analysis4.run(dataset)
            
        elif self.analysistype == '5a':
            dataset, proposedmean = datainput.input5a()
            analysis5a.run(dataset, proposedmean)
            
        elif self.analysistype == '5b':
            dataset1, dataset2 = datainput.input5b()
            analysis5b.run(dataset1, dataset2)
            
        elif self.analysistype == '5c':
            dataset1, dataset2 = datainput.input5c()
            analysis5c.run(dataset1, dataset2)
            
        elif self.analysistype.startswith('6'):
            x_values, y_values, y_errors = dataipnut.input6()
            if self.analysistype == '6a':
                analysis6a.run(x_values, y_values, y_errors)
            elif self.analysistype == '6b':
                analysis6b.run(x_values, y_values, y_errors)
            elif self.analysistype == '6d':
                analysis6d.run(x_values, y_values, y_errors)
            else:
                print("Invalid analysis type entered.")
                exit(1)
        elif self.analysistype == '7':
            pass # This will need to be implemented
        else:
            print("Invalid analysis type entered.")
            exit(1)
            
if __name__ == "__main__":
    StatsTool()

