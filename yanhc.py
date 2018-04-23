# coding: utf-8
import sql
import timestamp

def sqlformat(sql_file):
    sql.sqlformat(sql_file)

def get(time_str=None):
    return timestamp.get(time_str)

def totime(timestamp):
    return timestamp.totime(timestamp)

def now():
    return timestamp.now()

