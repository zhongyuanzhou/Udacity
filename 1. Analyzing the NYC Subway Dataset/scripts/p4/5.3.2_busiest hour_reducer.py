# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:14:18 2015

@author: jnyzio
"""

import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    For every single unit, write a reducer that will return the busiest datetime (e.g.,
    the entry that had the most entries).  Ties should go to datetimes that are later on in the
    Month of May.  You can assume that the contents of the reducer will be sorted by UNIT, such that
    all entries corresponding to a given UNIT will be sorted together. The output should be the UNIT
    name, the datetime (which is a concatenation of date and time), and ridership separated by tabs.
    For example, the output of the reducer may look like this:
    R001    2011-05-11 17:00:00	   31213.0
    R002	2011-05-12 21:00:00	   4295.0
    R003	2011-05-05 12:00:00	   995.0
    R004	2011-05-12 12:00:00	   2318.0
    R005	2011-05-10 12:00:00	   2705.0
    R006	2011-05-25 12:00:00	   2784.0
    R007	2011-05-10 12:00:00	   1763.0
    R008	2011-05-12 12:00:00	   1724.0
    R009	2011-05-05 12:00:00	   1230.0
    R010	2011-05-09 18:00:00	   30916.0
    ...
    ...
    Since you are printing the actual output of your program, you
    can't print a debug statement without breaking the grader.
    Instead, you should use the logging module, which we've configured
    to log to a file which will be printed when you hit "Test Run".
    For example:
    logging.info("My debugging message")
    '''

    max_entries = 0
    old_key = None
    datetime = ''
    this_key = ''
    for line in sys.stdin:
        data = line.split("\t")
       
        new_key = data[0]
        if old_key and old_key != new_key:
            value = '{0}\t{1}\t{2}'.format(old_key,datetime.strip(),max_entries)
            logging.info(value)
            print value
            
            new_count = data[1]
            max_entries = float(new_count)
            datetime = '{0} {1}'.format(data[2],data[3])
        else:
            new_count = float(data[1])
            if new_count >= max_entries:
                max_entries = float(new_count)
                datetime = '{0} {1}'.format(data[2],data[3])
             
        this_key = new_key
        old_key = this_key
        value_2 = '{0}\t{1}\t{2}'.format(old_key,datetime.strip(),max_entries)
        logging.info(value_2)
        print value_2
reducer()
