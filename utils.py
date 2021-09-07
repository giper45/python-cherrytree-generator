import calendar
import time

def timestamp():
    # Current GMT time in a tuple format
    current_GMT = time.gmtime()
    # ts stores timestamp
    ts = calendar.timegm(current_GMT)
    return ts

