# coding: utf-8
import sqlparse
import sys

def sqlformat(sql_file):
    f = open(sql_file, "r")
    for l in f:
        print sqlparse.format(l, reindent=True, keyword_case='upper')
