#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import csv
import sys



def yearfunc(year):
    if int(year)==2013:
        return int(year)
    else:
        return int(year) -1



in_data = pd.read_csv(sys.argv[1], header =  None, names=['year','index'])
# print in_data
in_data ['rank'] = in_data['index'].rank(ascending=1)
in_data['month'] = [(int((month-2013)*12)) for month in in_data['year']]
# print in_data

in_data ['year'] = [yearfunc(year) for year in in_data['year']]








print in_data
