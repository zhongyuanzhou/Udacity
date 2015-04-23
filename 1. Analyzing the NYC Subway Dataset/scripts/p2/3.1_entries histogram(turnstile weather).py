# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 13:41:32 2015

@author: jnyzio
"""

import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histograph may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
  
    plt.figure()
 
    #import data to graph
    # your code here to plot a historgram for hourly entries when it is raining
    turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==0].hist(bins = 18, alpha = 0.3, color = 'g', label = 'No Rain')
    # your code here to plot a historgram for hourly entries when it is not raining
    turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==1].hist(bins = 25, alpha = 0.8, color = 'b', label = 'Rain')

    #label the graph
    plt.title('Histogram of ENTRIESn_hourly.')
    plt.ylabel('Frequency')
    plt.xlabel('ENTRIESn_hourly')
    
    #legend referncing labels from data import
    plt.legend()
    return plt
