#!/usr/bin/env python

def binary_query(msg, default=True):
    '''
    Query the user with the yes/no question ``msg``. Return True if the response is yes, and
    return False if the response is no.
    '''
    if default == True:
        suffix = 'Y/n\n'
    else:
        suffix = 'y/N\n'
    response = input(msg + ' ' + suffix)
    if response.lower() == 'y' or response.lower() == 'yes':
        return True
    elif response.lower() == 'n' or response.lower() == 'no':
        return False
    # If the user response is not y/yes/n/no, call this function again, printing an error
    # message.
    else:
        binary("Invalid response.  Please type yes or no.", default=default)

def string_query(msg):
    '''
    Query the user with the question ''msg'', and return the string that the 
    user enters in response.
    '''
    print(msg)
    s = input('>>> ')
    return s
