# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:29:24 2019

@author: fengh
"""
import time

def LevDist(s_peak, s_len, t_peak, t_len):

    if s_len == 0:
        return t_len
    if t_len == 0:
        return s_len
    if s_peak[s_len - 1] == t_peak[t_len - 1]:
        cost = 0
    else:
        cost = 1
    
    if result[t_len-1][s_len-1] != -1:
        return result[t_len-1][s_len-1]
    res = min([LevDist(s_peak, s_len - 1, t_peak, t_len    ) + 1,
               LevDist(s_peak, s_len    , t_peak, t_len - 1) + 1, 
               LevDist(s_peak, s_len - 1, t_peak, t_len - 1) + cost])
    result[t_len-1][s_len-1] = res
    return res

def LevDist2(s, t):
    slen = len(s)
    tlen = len(t)
    result = [[0 for i in range(len(s))] for j in range(len(t))]
    cost = 0

    for i in range(tlen):
        result[i][0] = i
    for j in range(slen):
        result[0][j] = i

    for i in range(tlen):
        for j in range(slen):
            if s[j-1] == t[i-1]:
                cost = 0
            else:
                cost = 1

            result[i][j] = min([result[i-1][j]+1,
                                result[i][j-1]+1,
                                result[i-1][j-1]+cost])
    return result[tlen-1][slen-1]

if __name__ == '__main__':
    
    start = time.time()
    realPeaks = ['6', '7', '8', '9', '10', '9', '8', '6', '7', '8', '7', '8', 
                 '6', '7', '8', '9', '10', '9', '8', '6', '7', '8', '7', '8']
    r_len = len(realPeaks)

    orgPeaks = ['1', '2', '1', '2', '10', '9', '8', '6', '7', '8', '2', '8',
                '6', '7', '8', '9', '10', '9', '8', '6', '7', '8', '7', '8']
    o_len = len(orgPeaks)
    result = [[-1 for i in range(len(realPeaks))] for j in range(len(orgPeaks))]
#    diff = LevDist2(realPeaks, orgPeaks)
    diff = LevDist(realPeaks, r_len, orgPeaks, o_len)
    sim = 1 - (float(diff)/(float(o_len)))
    end = time.time()
    print("stft time: " + str(end - start))
    print(diff, sim)