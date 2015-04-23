# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 13:48:04 2015

@author: jnyzio
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys

def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.
    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    
  #define the cost history 
    cost_history = []
    
    #sum of square errors is the sum of difference of the dot product of specified variables.
    # np.square the results
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    
    #for loop through iterations 
    for i in range(num_iterations):
        
        #append compute_cost to the cost history using the specified variables.
        cost_history.append(compute_cost(features, values, theta))
        
        #set error equal to the values minus the dot product of features and theta
        error = values - np.dot(features, theta) 
        
        #theta is the weighted capacity for x to determine the value of y within the dataset.
        #find theta using a variation of the linear regression with gradient decent equation from 3d slide. 
        theta = theta + (alpha/(2*m))*np.dot(error, features)
    return theta, pandas.Series(cost_history)
'''
    numerator = np.square(data - predictions).sum()
    mean = np.mean(data)
    denominator = np.square(data - mean).sum()
    r_squared = 1 - (numerator / denominator)
    
    return r_squared