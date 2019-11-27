# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:10:02 2019

@author: fengh
"""
import stft
import numpy as np
import random
import csv
import sys
import datetime

def create(bank):
    
   len_choice = [5,6,7,8,9]
   n = random.choice(len_choice)
   source = []
   for i in range(n):
       source.append(random.choice(bank))
       
   return source

now = datetime.datetime.now()

bank = ['1','2','3','4','5','6','7','8','9','a','b']
fileName = 'Lev_accuracy' + '.csv'

try:
    with open(fileName, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['number of test', 'target', 'source', 'result'])
except csv.Error as e:
    sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
    

#target = ['4','7','3','a','9','1','b','8','2']


for i in range(2):
    
    source = create(bank)

    result = stft.LevDist2(source,target)
    print(i)
    
    try:
        with open(fileName, 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', 
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([i, target, source, result])
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
                
                
            