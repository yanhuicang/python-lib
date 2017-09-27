# coding: utf-8
from datetime import datetime
import time
import math

def get():
    d = datetime.now()
    t = d.timetuple()
    timeStamp = int(time.mktime(t))
    ms = int(round(d.microsecond / 1000.0))
    timeStamp = "%d.%d" % (timeStamp, ms)
    print timeStamp

if __name__ == "__main__":
    get()
