#Zimian Li
#Q3
import random
import time
import math

count0 = 0
count1 = 0

def genList(n, upper):
    lst = []
    for i in range(n):
        lst.append(random.randint(1,upper))
    return lst

#A greedy algorithm
#it can just find an approximate solution
def minProc(A, t):
    #Array A should be sorted
    #A.sort()
    procs = {}
    if (t < A[len(A)-1]):
        return None
    
    head = 0
    pid = 0
    
    for i in range(len(A)-1, -1, -1):
        if i < head:
            break
        if i == head:
            procs[pid] = [A[i]]
            break
        
        procs[pid] = [A[i]]
        if A[i] == t:
           pid += 1
        else:
            sums = A[i]
            for j in range(head, i):
                sums += A[j]
                if sums > t:
                    pid += 1
                    break
                else: #sums <= t
                    procs[pid].append(A[j])
                    head += 1
    return procs        

def minTime(A, p):
    A.sort()
    approx_t = A[len(A)-1]

    #it must stop, because min t is between max of A and sum of A
    while approx_t :
        procs = minProc(A, approx_t)
        if(len(procs) <= p):
            return procs
        else:
            approx_t += 1

    return None


def printResult(p, n, upper):
    lst = genList(n, upper)
    procs = minTime(lst, p)
    print(lst)
    print(procs)

def pR(A, p):
    procs = minTime(A, p)
    print(A)
    print(procs)
    
