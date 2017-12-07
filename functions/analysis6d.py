#!/usr/bin/env python
import numpy
import scipy.stats
import functions.regression as regression
import matplotlib.pyplot as pyplot

'''
Perform a linear regression.
'''
def run(x_values, y_values, y_errors):
    '''
    -----------
    Parameters:
    -----------
    x_values: (numpy.ndarray) a 1-dimensional numpy array of x-values
    y_values: (numpy.ndarray) a 1-dimensional numpy array of y-values, where
        for each i=1,2,...,n x_values[i] is paired with y_values[i].
    y_errors: (numpy.ndarray or None) the errors associated with each value

    -----------------
    Function
    -----------------
    Perform a linear regression and show the resulting plot.
    '''
    m, sigma_m, b, sigma_b, r, p = regression.linear(x_values, y_values, y_errors) 

    def bestfit(x):
        '''
        Return the value of the best fit line at position x
        '''
        return m*x+b

    residuals = y_values - bestfit(x_values)

    xmin = x_values.min()
    xmax = x_values.max()
    ymin = bestfit(x_values).min()
    ymax = bestfit(x_values).max()

    fig, (ax1, ax2) = pyplot.subplots(1, 2)

    # Plot line of best fit
    ax1.plot((xmin, xmax), (bestfit(xmin), bestfit(xmax)), color='black') 
    # plot original data
    if y_errors is None:
        ax1.plot(x_values, y_values, 'o', color='black')
    else:
        ax1.errorbar(x_values, y_values, yerr = y_errors, color='black')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('linear regression and input data')

    # Plot residuals on separate plot
    ax2.plot(bestfit(x_values), residuals, 'o', color='black')
    ax2.plot((ymin, ymax), (0, 0), color='black', linestyle='dashed')
    ax2.set_xlabel('y')
    ax2.set_ylabel('Residual from linear regression')
    ax2.set_title('Residuals')

    # Print a table for the user
    msg = '''
--------------------------------------------------------------------------------
Linear regression
--------------------------------------------------------------------------------
slope: {:.04e} +/- {:.04e}
y-intercept: {:.04e} +/- {:.04e}
p: {:.04e}

Note: ``p`` is the probability of observing a correlation at least as strong as
      that observed in the specified samples, given that the variables are
      uncorrelated.
'''.format(m, sigma_m, b, sigma_b, p)
    print(msg)
    pyplot.show()
