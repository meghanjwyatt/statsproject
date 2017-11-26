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

def input1():
    '''
    Get input for a Q-Q plot of x/y data
    '''
    msg1 = "Please enter the first sample."
    dataset1 = UserDataSet(msg1).data
    
    msg2 = ("Please enter the second sample, which should be the same length "
           "as the first sample.")
    dataset2 = UserDataSet(msg2, requiredsize=dataset1.shape[0]).data
    
    return dataset1, dataset2

def input2():
    '''
    Get input computing mean confidence limits.
    '''
    msg = "Please enter the values of the sample."
    dataset = UserDataSet(msg).data
    return dataset

def input3():
    '''
    Get input for computing confidence limits for the difference between two samples
    '''
    msg1 = "Please enter the first sample."
    dataset1 = UserDataSet(msg1).data
    
    msg2 = "Please enter the second sample."
    dataset2 = UserDataSet(msg2).data
    return dataset1, dataset2

def input4():
    '''
    Get input for computing confidence limits of a sample using simulation
    '''
    msg = "Please enter the values of the sample."
    dataset = UserDataSet(msg).data
    return dataset

def input5a():
    '''
    Get input for testing the hypothesis that the mean of a specified sample is 
    equal to a specified value.
    '''
    msg = "Please enter the values of the sample."
    dataset = UserDataSet(msg).data
    proposedmean = float(input("Please enter the proposed mean"))
    return dataset, proposedmean

def input5b():
    '''
    Get input for testing whether there is a difference between two means.
    '''
    msg1 = "Please enter the values of the first sample."
    dataset1 = UserDataSet(msg1).data
    msg2 = "Please enter the values of the second sample."
    dataset2 = UserDataSet(msg2).data
    return dataset1, dataset2

def input5c():
    '''
    Get input for a chi-squared test.
    '''
    msg1 = "Input the number of values in each category, for the first group."
    dataset1 = UserDataSet(msg1).data
    msg2 = "Input the number of values in each category, for the second group."
    dataset2 = UserDataSet(msg2).data
    return dataset1, dataset2

def input6():
    '''
    Get input for calculating correlation coefficient of x/y data, carrying 
    out hypothesis testing on the correlation coefficient, or performing a linear
    regression on the x/y data.
    
    Return the following:
        x_values: numpy array of the x values
        y_values: numpy array of the y values, where the i^th y value
            corresponds to the i^th x value.
        y_errors: if specified, a numpy array of error bars (e.g., standard
            deviations) for the y values. If not specified, return None.
    '''
    msg1 = "Input the x values."
    x_values = UserDataSet(msg1).data
    msg2 = ("Input the y values. The number of y values should be the same as the "
           "number of x values, and the i^th y value should correspond to the "
           "i^th x value.")
    y_values = UserDataSet(msg2, requiredsize = x_values.shape[0]).data
    # Query the user regarding the inclusion of error bars
    includeerrorbars = binary_query("Would you like to include error bars?")
    if includeerrorbars:
        msg3 = "Input the error bars associated with y values."
        y_errors = UserDataSet(msg3, requiredsize = x_values.shape[0]).data
    else:
        y_errors = None
    return x_values, y_values, y_errors

def binary_query(msg, default=True):
    '''
    Query the user with the yes/no question ``msg``. Return True if the response is yes, and
    return False if the response is no.
    '''
    if default == True:
        suffix = 'Y/n'
    else:
        suffix = 'y/N'
    response = input(msg + ' ' + suffix)
    if response.lower() == 'y' or response.lower() == 'yes':
        return True
    elif response.lower() == 'n' or response.lower() == 'no':
        return False
    # If the user response is not y/yes/n/no, call this function again, printing an error
    # message.
    else:
        binary_query("Invalid response.  Please type yes or no.", default=default)
    

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
            self.load_from_file()
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
                              "the Enter key.")
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
            
