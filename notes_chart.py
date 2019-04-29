# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:09:48 2019

@author: CV_LAB_Howard
"""
import pandas
import csv
import sys

notes = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0,
         5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5]
n= len(notes)
rows = n
cols = n
diff = [[0 for x in range(cols)] for x in range(rows)]
fileName = 'note_diff.csv'

for col in range(cols):
    for row in range(rows):
        diff[row][col] = abs(notes[row] - notes[col])

for r in range(rows):
    
    with open(fileName, 'a') as csvfile:
        try:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(diff[r])
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))