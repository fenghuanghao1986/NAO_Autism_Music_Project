# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:09:48 2019

@author: CV_LAB_Howard
"""
import pandas

notes = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 4.5, 5.0, 5.5, 6.0,
         6.5, 7.0, 8.0, 8.5, 9.0, 9.5, 10.0, 11.0]
n= len(notes)
rows = n
cols = n
diff = [[0 for x in range(cols)] for x in range(rows)]

for col in range(1, cols):
    for row in range(1, rows):
        diff[row][col] = abs(notes[col] - notes[row])

for r in range(rows):
    print(diff[r])
    
