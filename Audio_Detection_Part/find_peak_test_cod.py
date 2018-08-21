# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 18:04:03 2018

@author: fengh
"""

data = [1, 1.1,1.2, 1.3, 1.5, 1.6 , 1.7 , 1.8,  2, 3, 2, 3, 4, 3, 4, 5, 4, 3, 1.8]
 
#每个顶点的index， D（Down）,U(Up)
apex_index = []
 
#趋势-1(Down), 0, 1(Up)
qs = 0
 
#偏离值和偏离百分比
plz_p = 0.2
 
#当前值
min_index = max_index = 0
 
for index, num in enumerate(data):
 
    min_dqz = data[min_index]
    max_dqz = data[max_index]
     
    min_plz = min_dqz * plz_p
    max_plz = max_dqz * plz_p
     
    #print '='*10, index, '='*10
    #print 'plz:', num - min_dqz, min_plz, 'qs:', qs, 'min_index:', min_index, 'up'
    #print 'plz:', num - max_dqz, max_plz, 'qs:', qs, 'max_index:',  max_index, 'down'
     
    #上升
    if (num - min_dqz ) >0:
 
        if (num - min_dqz- min_plz) > 0:
            if qs != 1:
                apex_index.append( 'U%s'%min_index )
                max_index = index
                max_dqz = num
                #print 'U%s'%min_index
            qs = 1
         
     
    #下降
    if (num - max_dqz) <0:
        if (num - max_dqz) < -max_plz:
            if qs!=-1:
                apex_index.append( 'D%s'%max_index )
                min_index = index
                min_dqz = num
                #print 'D%s'%max_index
            qs = -1
         
    if num > max_dqz:
        max_index = index
         
    if num < min_dqz:
        min_index = index
     
print(apex_index, qs, max_index, min_index)
#raw_input()
import matplotlib.pyplot as plt
plt.plot(data)