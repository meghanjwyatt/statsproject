#!/usr/bin/env python
import numpy

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
        sample_mean = synthetic_sample.mean()
        # append mean to sample_means (list)
        sample_means.append(sample_mean)
        
    # Calculate the confidence interval of sample means
    # first, order the sample means
    sample_means.sort()
    
    # lower confidence limit
    lcl = numpy.percentile(sample_means, 100*alpha/2)
    
    # upper confidence limit
    ucl = numpy.percentile(sample_means, 100*(1-alpha/2))
    
    print("The {:.04f}% confidence interval for the mean of the given sample is {:.04e} to {:.04e}"\
          .format(100*(1-alpha), lcl, ucl))
    
