# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:00:14 2019

@author: CV_LAB_Howard
"""

# for loop test


tasks = [1, 2, 3, 666]

for i in range(1000):
    i = int(raw_input("select tasks: "))
    if i == 1:
        print("task one starts")
    elif i == 2:
        print("task two starts")
    elif i == 3:
        print("task tree starts")
    elif i == 666:
        break
    else:
        continue

