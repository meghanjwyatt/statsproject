#!/usr/bin/env python
import numpy
import loaddata.query
from loaddata.data import UserDataSet

def input1():
    '''
    Get input for a Q-Q plot of x/y data
    '''
    msg = "Please enter the first sample."
    dataset = UserDataSet(msg).data
    return dataset

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
    proposedmean = float(input("Please enter the proposed mean and press then "
                               "press the enter key\n"))
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
    datasets = []
    msg1 = "Input the number of values in each category, for the first group."
    datasets.append(UserDataSet(msg1).data)
    msg2 = "Input the number of values in each category, for the second group."
    datasets.append(UserDataSet(msg2).data)

    dataset_idx = 3
    add_dataset = query.binary_query("Enter another sample?")
    while add_dataset:
        msg = "Input the number of values in ech category, for group #{:d}"\
              .format(dataset_idx)
        datasets.append(UserDataSet(msg).data)
        dataset_idx += 1

    return datasets

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
    includeerrorbars = query.binary_query("Would you like to include error bars?")
    if includeerrorbars:
        msg3 = "Input the error bars associated with y values."
        y_errors = UserDataSet(msg3, requiredsize = x_values.shape[0]).data
    else:
        y_errors = None
    return x_values, y_values, y_errors

def input7():
    '''
    Get input for performing propagation of error.
    Return the following:
        variable_values: The value of variables a, b, c, ...     
        variable_errors: The value of the errors associated with 
                         variables a, b, c, ...
        calculation_str: A string specifying the calculation to be performed.
    '''
    msg = '''
--------------------------------------------------------------------------------
Propagation of error 

How to:
    In the first data set, input the value of each variable. In the second data 
    set, input the errors associated with each variable (in the corresponding 
    order). Variables are labelled with letters a-z in the order in which they
    are input; a maximum of 26 variables are allowed.  Once the variables and 
    associated uncertainties are entered, specify the calculation using the
    following syntax:
        + : addition
        - : subtraction
        * : multiplication
        / : division
        ** : exponentiation
        ln(value) : natural logarithm of value
        
    For example, you could enter:
        a+b: find the sum of the first two numbers entered, as well as the 
             associated error.
        a-b*c: find the difference between a and (b times c), as well as the
               associated error.
        a**b: calculate a to the b power, and the associated error

--------------------------------------------------------------------------------
'''

    msg1 = "Input the variables' values."
    values = UserDataSet(msg1).data
    msg2 = ("Input the uncertainties associated with each variable, in the same \n" +\
            "order as which the values were specified")
    uncertainties = UserDataSet(msg2, requiredsize=values.shape[0]).data
    msg3 = "Input the expression for the desired calculation."
    expression = query.string_query(msg3)
    return values, uncertainties, expression
