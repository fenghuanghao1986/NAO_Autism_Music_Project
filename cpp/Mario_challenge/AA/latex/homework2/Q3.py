#Zimian Li
#Q3
import random
import time
import math


def genBoundList(n, lower, upper):
    lst = []
    for i in range(n):
        lst.append(random.randint(lower,upper))
    return lst

#A greedy algorithm
def minProc(A, t):
    #t must be greater than the max in A
    procs = []
    cap = 0
    
    for i in range(len(A)):
        global count0
        count0 += 1
        
        cap += A[i]
        if (i == len(A)-1):
            procs.append(i)
        elif (cap + A[i+1] > t):
            cap = 0
            procs.append(i)
    
    return procs        

def minTime(A, p):
    #1 <= p <= len(A)
    approx_t = max(math.ceil(sum(A)/p),max(A))

    #it must stop, because min t is between max of A and sum of A
    while approx_t :
        procs = minProc(A, approx_t)
        if(len(procs) <= p):
            return procs
        else:
            approx_t += 1

    return None

def looper(A, start, depth, out):
    global mint
    global result
    global count1
    count1 += 1

    #not enough depth
    if (start >= len(A)):
        return

    #get one combination and compare it
    if (depth <= 0):
        out.append(len(A)-1)
        mint1 = updateMin(A, out, mint)
        if (mint1 < mint) or (mint == 0):
            result = out[:]
            mint = mint1
        out.pop()
    else:
        for i in range(start, len(A) - depth + 1):
            out.append(i)
            looper(A, i+1, depth-1, out)
            out.pop()

def updateMin(A, B, mint):
    ib = 0
    localmax = 0
    sub = 0
    for i in range(len(A)):
        sub += A[i]
        if i == B[ib]:
            if sub > localmax:
                localmax = sub
            sub = 0
            ib += 1

    return localmax
        
def minTimeBF(A, p):
    global mint
    global result
    
    mint = 0
    result = []

    for i in range(len(A)-p+1):
        lst = [i]
        looper(A, i+1, p-2, lst)

    return result        

def printResult(p, n):
    global count0
    global count1
    count0 = 0
    count1 = 0
    lst = genBoundList(n, 1, 100)
    time0 = time.clock()
    result0 = minTime(lst, p)
    time1 = time.clock()
    result1 = minTimeBF(lst, p)
    time2 = time.clock()

    print("Input size: n = ", n, ", p = ", p)
    print("Result: greedy - ", result0, ", brute force - ", result1)
    print("Loops: greedy - ", count0, ", brute force - ", count1)
    print("Time: greedy - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def test():
    print("Problem 3:")
    printResult(4, 10)
    printResult(4, 100)
    printResult(5, 100)
