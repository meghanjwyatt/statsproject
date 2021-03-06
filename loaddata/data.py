#!/usr/bin/env python
import numpy

'''
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

class UserDataSet(object):
    '''
    Framework for loading user-specified data. Enables input of data via files
    or via ``manual`` user input. Load a single data set.
    '''
    def __init__(self, msg, requiredsize=None):
        self.requiredsize = requiredsize 
        self.load(msg=msg)
        
    def load(self, msg=''):
        self.prompt_user(msg)
        if self.use_file_input:
            try:
                self.load_from_file()
            except FileNotFoundError:
                print('File "{:s}" not found! Did you mean to enter data '
                      'manually?'.format(self.inputfilepath))
                self.load()
        else:
            self.load_manually()
        self.check_data()
        
    def prompt_user(self, msg):
        '''
        Prompt the user with the message ``msg``, and ask the user whether
        data should be entered via a file or manually.
        '''
        print(msg)
        inputfilepath = input("If you wish to load data from a file "
                              "(newline-buffered, ASCII-format), enter the "
                              "file name here. To enter data manually, press "
                              "the Enter key.\n")
        if inputfilepath.strip() == '':
            self.use_file_input = False
        else:
            self.use_file_input = True
            self.inputfilepath = inputfilepath
            
        
    def load_from_file(self):
        self.data = numpy.loadtxt(self.inputfilepath)
        
    def load_manually(self):
        print("Begin entering data. After each data point, press the Enter "
              "key. When you are finished entering data, type ``done`` and "
              "press the Enter key.")
        
        # Data is a list that will grow as the user enters data.  It will store
        # the numerical data.
        data = []
        
        # the user input (a string). Initialize this variable here, prior to the 
        # while-loop
        inputstr = ''
        
        # the .lower() method converts inputstr to lowercase, in case the user
        # enters something like "Done" or "DONE" instead of "done" (lowercase).
        # Check if the user is finished entering values for this data set.
        while inputstr.lower() != 'done':
            inputstr = input()
            
            # If the user entered what looks like a numerical value
            if inputstr.lower() != 'done':
                # Try converting the user input to a float
                try:
                    data.append(float(inputstr))
                # if the string to float conversion fails, tell the user that
                # the data format is invalid, and ask the user to enter the data
                # again.
                except ValueError:
                    print("Invalid input format.  Please enter the value again "
                          "using one of the following formats:\n"
                          "  1.234\n"
                          "  1.234e+4\n"
                          "  1234")
        # At this point, the user has finished entering the data. Now just convert
        # the list to a numpy array, for consistency with self.load_from_file
        self.data = numpy.array(data)
        
    def check_data(self):
        if self.data.ndim > 1:
            print("The file you specified contains multiple columns of data. Please "
                  "specify a file containing only a single column of numerical data.")
            self.load()
        if not self.requiredsize is None and self.data.shape[0] != self.requiredsize:
            print("The data set required should have length {:d}, but a data set of "
                  "length {:d} was entered. Please re-enter the data set."\
                  .format(self.requiredsize, self.data.shape[0]))
            self.load()
            
