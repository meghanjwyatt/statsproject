#!/usr/bin/env python

'''
Compute mean confidence limits via simulation
'''
def run(dataset, alpha=0.05):
    # number of synthetic samples to generate
    nsamples = 1000
    
    # A list that will hold the mean of each synthetic sample
    sample_means = []
    
    # range(nsamples) will look like [0, 1, 2, ..., nsamples-1]
    for isample in range(nsamples):
        # generate synthetic sample
        synthetic_sample = numpy.random.choice(dataset, size=len(dataset))
        # calculate mean of synthetic sample
        
        # append mean to sample_means (list)
       
    
