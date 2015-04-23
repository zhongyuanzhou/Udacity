# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 13:46:40 2015

@author: jnyzio
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    
    plt.figure()
    #determine residuals by determining the difference of the hourly entries column and our predictions.
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins = 80, label = 'Residuals')
    plt.title('Difference between original and predicted hourly entry values')
    plt.ylabel('Frequency')
    plt.xlabel('ENTRIESn_hourly')
    #call the legend created in line 19
    plt.legend()
    return plt