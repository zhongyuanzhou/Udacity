# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 16:55:03 2015

@author: jnyzio
"""

import datetime
import time 

def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    Hint: 
    There is a useful function in the datetime library called strptime. 
    More info can be seen here:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''
    #Use strptime and set index values using x 
    date_formatted = x = time.strptime(date, "%m-%d-%y")
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    
    #format by index using datetime and strftime
    date = datetime.datetime(x[0], x[1], x[2])
    date_formatted = date.strftime("%Y-%m-%d")

    return date_formatted
