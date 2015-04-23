# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:12:49 2015

@author: jnyzio
"""

import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this assignment, the reducer should
    print one row per weather type, along with the average value of
    ENTRIESn_hourly for that weather type, separated by a tab.  You can assume
    that the input to the reducer will be sorted by weather type, such that all
    entries corresponding to a given weather type will be sorted together.
    In order to compute the average value of ENTRIESn_hourly, you'll need to
    keep track of both the total riders per weather type and the number of
    hours with that weather type.  Then when you are ready to output the
    result, you can divide the total riders by the number of hours.  That's why
    we initialized both riders and num_hours below.
    One example output row might look like this:
    fog-norain   1105.32467557
    Since you are printing the actual output of your program, you
    can't print a debug statement without breaking the grader.
    Instead, you should use the logging module, which we've configured
    to log to a file which will be printed when you hit "Test Run".
    For example:
    logging.info("My debugging message")
    '''

    riders = 0      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None
    entries = 0
    for line in sys.stdin:
        data = line.split("\t")
        
        new_value = "{0}\t{1}".format(data[0],data[1])
        this_key = data[0]
        if old_key and old_key != this_key:
            count = "{0}\t{1}".format(old_key,(1.0*riders/num_hours))
            logging.info(count)
            print count
            
            riders = float(data[1])
            num_hours = 1
        else:
            riders = riders + float(data[1])
            num_hours += 1
            
        old_key = this_key
        logging.info(new_value.strip())

    last_key = "{0}\t{1}".format(old_key,(1.0*riders/num_hours))
    print last_key
reducer()
