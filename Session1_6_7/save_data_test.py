# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:55:59 2019

@author: fengh
"""

# read and write data test function

import numpy as np
import csv
import datetime

print "Enter subject number:\n"
subject = raw_input()
print "Enter session number:\n"
session = raw_input()
now = datetime.datetime.now()
day = str(now.day)
mon = str(now.month)
year = str(now.year)

fileName = subject + '_' + session  + '_' + year + '_' + mon + '_' + day

with open(fileName + '.csv', 'a') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    filewriter.writerow(['task', 'ground_truth', 'kid_input', 'result'])
    filewriter.writerow(['01', '123', '122', '.667'])
    filewriter.writerow(['01', '123', '122', '.667'])
    filewriter.writerow(['01', '123', '122', '.667'])

