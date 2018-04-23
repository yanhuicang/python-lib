# coding: utf-8
from datetime import datetime
import time
import math

def get(time_str=None):
    if time_str is None:
        d = datetime.now()
    else:
        d = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
    t = d.timetuple()
    timeStamp = int(time.mktime(t))
    ms = int(round(d.microsecond / 1000.0))
    timeStamp = "%d%03d" % (timeStamp, ms)
    return timeStamp

def totime(timestamp):
    f = float(timestamp) / 1000
    d = datetime.fromtimestamp(f)
    t = d.strftime("%Y-%m-%d %H:%M:%S.%f")
    return t

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

if __name__ == "__main__":
    t = get("2017-09-26 00:10:10.101")
    print t
    print totime(t)
