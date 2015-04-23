# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:01:48 2015

@author: jnyzio
"""

from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    plot = ggplot(aes(x='Hour', y='ENTRIESn_hourly', color = 'rain'), data=turnstile_weather) + \
    geom_point() + \
    ggtitle("Hourly NYC subway entries on rainy and non rainy days") + \
    xlab("Hour") + \
    ylab("ENTRIESn_hourly") + ylim(0, 45000) \
    + xlim(-1, 24) + scale_x_continuous(breaks=[0,3,6,9,12,15,18,21,24],  \
    labels=["12:00am", "3:00am", "6:00am", "9:00am", "12:00pm", "3:00pm", "6:00pm", "9:00pm"]) +\
    facet_grid('rain', scales = "free")
    theme_seaborn() 
                                     
    return plot
