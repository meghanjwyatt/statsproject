#!/usr/bin/env python
import numpy
import uncertainties

'''
Calculate and print uncertainties in a user-defined expression.
'''
def run(values, errors, expression):
   '''
   --------------
   Parameters
   --------------
   values: (numpy.ndarray) An array of values, where the i^th position of
           values is associated with the i^th letter of the alphabet.
   errors: (numpy.ndarry) An array of uncertainties associated with the values
           in ``values``, in the same order.
   expression: (str) An expression denoting the user-specified calculation to 
           perform.  Valid operations include +, -, *, /, **, ln()
   '''
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   
   # Check that there are a maximum of 26 values in ``values``
   if len(values) > 26:
       raise ValueError("Error! At maximum, you can import 26 values. Exiting...")
   
   variables = {}
   for ival, value in enumerate(values):
       error = errors[ival]
       var_symbol = alphabet[ival]
       # Probably some security issues here...
       to_evaluate = "{:s} = uncertainties.ufloat({:s}, {:s})".format(var_symbol,
                                                                      repr(value),
                                                                      repr(error))
       # Create the variable
       exec(to_evaluate)
   result = eval(expression)
   print("Result of {:s} is: {:s}".format(expression, str(result)))
       
