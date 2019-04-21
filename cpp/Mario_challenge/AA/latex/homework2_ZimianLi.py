#Zimian Li
#Homework 2
import random
import time
import math
import os

#--------------------Problem 1------------------#
#Generate a random sorted list in range (260, 340)
def genSortedList(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(260,340))
    lst.sort()
    return lst

#Find the last one's index with the given score
def findUpper(A, x, p, r):
    global count0
    count0 += 1
    mid = (p+r)//2
    if (A[mid] != x) and ((p >= r) or (mid <= 0) or (mid >= len(A)-1)):
        return None
    elif (A[mid] == x) and ((p >= r) or (mid <= 0) or (mid >= len(A)-1)):
        return mid
    elif(A[mid] == x) and (A[mid+1] > A[mid]):
        return mid
    elif A[mid] > x:
        return findUpper(A, x, p, mid-1)
    elif (A[mid] < x) or ((A[mid] == x) and (A[mid+1] == x)):
        return findUpper(A, x, mid+1, r)

#My algorithm, find all scores 260 to 340 by findUpper
def countScores(A):
    result = {}
    lower = 0
    for x in range(260,341):
        upper = findUpper(A, x, lower, len(A)-1)
        if upper == None:
            result[x] = 0
        else:
            result[x] = upper - lower + 1
            lower = upper + 1
    return result

#A native brute force algorithm
def countScoresBF(A):
    result = {}
    global count1
    for e in A:
        count1 += 1
        if e in result:
            result[e] += 1
        else:
            result[e] = 1
    return result

def printResultP1(n):
    global count0
    global count1
    count0 = 0
    count1 = 0
    lst = genSortedList(n)
    time0 = time.clock()
    result0 = countScores(lst)
    time1 = time.clock()
    result1 = countScoresBF(lst)
    time2 = time.clock()

    print("Input size: ", n)
    #print("Input array: ", lst)
    #print("Result: my algorithm - ", result0, ", brute force - ", result1)
    print("Loops: my algorithm - ", count0, ", brute force - ", count1)
    print("Time: my algorithm - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def testP1():
    print("--------------------------------Problem 1---------------------------------")
    printResultP1(10)
    printResultP1(1000)
    printResultP1(100000)
    #printResultP1(10000000)

#--------------------Problem 2------------------#
def genPointList(n):
    lst = []
    for i in range(n):
        x = round(random.uniform(0,100),2)
        y = round(random.uniform(0,100),2)
        lst.append([x,y])
    return lst

#return [min_x, min_y, max_x, max_y]
#DAC
def findBoundingBoxDAC(A, p, r):
    global count0
    if (r - p) == 1:
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0
        if A[p][0] < A[r][0]:
            min_x = A[p][0]
            max_x = A[r][0]
        else:
            min_x = A[r][0]
            max_x = A[p][0]
        if A[p][1] < A[r][1]:
            min_y = A[p][1]
            max_y = A[r][1]
        else:
            min_y = A[r][1]
            max_y = A[p][1]
        count0 += 2
        return [min_x, min_y, max_x, max_y]
    if p == r:
        return [A[p][0], A[p][1], A[p][0], A[p][1]]
    
    mid = (p+r)//2
    #To make sure at most pairs at last
    if (mid%2 == 0):
        mid += 1
    
    lst0 = findBoundingBoxDAC(A, p, mid)
    lst1 = findBoundingBoxDAC(A, mid+1, r)
    
    count0 += 4
    min_x = lst0[0]
    min_y = lst0[1]
    max_x = lst0[2]
    max_y = lst0[3]
    if(min_x > lst1[0]):
        min_x = lst1[0]
    if(min_y > lst1[1]):
        min_y = lst1[1]
    if(max_x < lst1[2]):
        max_x = lst1[2]
    if(max_y < lst1[3]):
        max_y = lst1[3]
    return [min_x, min_y, max_x, max_y]


#brute force
def findBoundingBoxBF(A):
    min_x = A[0][0]
    min_y = A[0][1]
    max_x = A[0][0]
    max_y = A[0][1]

    global count1
    for i in range(1,len(A)):
        count1 += 4
        if (A[i][0] < min_x):
            min_x = A[i][0]
            count1 -= 1
        elif (A[i][0] > max_x):
            max_x = A[i][0]
        
        if (A[i][1] < min_y):
            min_y = A[i][1]
            count1 -= 1
        elif (A[i][1] > max_y):
            max_y = A[i][1]
            
    return [min_x, min_y, max_x, max_y]
        
    
def printResultP2(n):
    global count0
    global count1
    count0 = 0
    count1 = 0
    lst = genPointList(n)
    time0 = time.clock()
    result0 = findBoundingBoxDAC(lst, 0, n-1)
    time1 = time.clock()
    result1 = findBoundingBoxBF(lst)
    time2 = time.clock()

    print("Input size: ", n)
    #print("Input array: ", lst)
    print("Result: DAC - ", result0, ", brute force - ", result1)
    print("Comparisons: DAC - ", count0, ", brute force - ", count1)
    print("Time: DAC - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def testP2():
    print("--------------------------------Problem 2---------------------------------")
    printResultP2(10)
    printResultP2(1000)
    printResultP2(100000)
    printResultP2(100001)
    #printResultP2(10000000)

#--------------------Problem 3------------------#
def genBoundList(n, lower, upper):
    lst = []
    for i in range(n):
        lst.append(random.randint(lower,upper))
    return lst

#A greedy algorithm
#given t, minimize p
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

#Iterate some times of minProc to get the exact answer
#given p, minimize t
def minTime(A, p):
    #1 <= p <= len(A)
    #get the greater one between the sum(A)/p and the max of A, O(n)
    approx_t = max(math.ceil(sum(A)/p),max(A))

    #it must stop, because min t is between max of A and sum of A
    procs = minProc(A, approx_t)
    while (len(procs) > p):
        approx_t += 1
        procs = minProc(A, approx_t)

    return procs

#A helper function for brute force algorithm
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

#A brute force algorithm        
def minTimeBF(A, p):
    global mint
    global result
    
    mint = 0
    result = []

    for i in range(len(A)-p+1):
        lst = [i]
        looper(A, i+1, p-2, lst)

    return result        

def printResultP3(p, n):
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
    #print("Input array: ", lst)
    print("Result: greedy - ", result0, ", brute force - ", result1)
    print("Loops: greedy - ", count0, ", brute force - ", count1)
    print("Time: greedy - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def testP3():
    print("--------------------------------Problem 3---------------------------------")
    printResultP3(4, 10)
    printResultP3(4, 100)
    printResultP3(5, 100)

#--------------------Problem 4------------------#
def genList1D(n):
    lst = []
    for i in range(n):
        #lst.append(random.randint(0,n))
        lst.append(i)
    random.shuffle(lst)
    return lst

def genList2D(n):
    lst = []
    for i in range(n):
        sub = []
        for j in range(n):
            #sub.append(j)
            #random.shuffle(sub)
            sub.append(random.randint(0,n))
        lst.append(sub)
    return lst

#1D: binary search
def findLocalMax1D(A, p, r):
    global count0
    count0 += 1
    if (len(A) == 0):
        return None
    if (len(A) == 1):
        return 0
    
    mid = (p+r)//2
    if (mid == 0):
        if (A[mid] >= A[mid+1]):
            return mid
    elif (mid == len(A)-1):
        if (A[mid] >= A[mid-1]):
            return mid
    elif (A[mid] >= A[mid-1]) and (A[mid] >= A[mid+1]):
        return mid
    elif (A[mid] < A[mid-1]):
        return findLocalMax1D(A, p, mid-1)
    elif (A[mid] < A[mid+1]):
        return findLocalMax1D(A, mid+1, r)

#1D: brute force
def findLocalMax1DBF(A):
    global count1
    if (len(A) == 0):
        return None
    if (len(A) == 1):
        return 0

    for i in range(len(A)):
        count1 += 1
        if (i == 0):
            if (A[i] >= A[i+1]):
                return i
        elif (i == len(A)-1):
            if (A[i] >= A[i-1]):
                return i
        elif (A[i] >= A[i-1]) and (A[i] >= A[i+1]):
            return i

#find the max of an array, O(n)
def findMax1D(A):
    global count0
    maxValue = A[0]
    maxIndex = 0
    for i in range(1, len(A)):
        count0 += 1
        if A[i] > maxValue:
            maxValue = A[i]
            maxIndex = i
    return maxIndex
    
#2D: binary search
def findLocalMax2D(A, p, r):
    global count0
    count0 += 1
    #ignore all other conditions like A is empty or A is 1D
    xmid = (p+r)//2
    ymax = findMax1D(A[xmid])

    if (xmid == 0):
        if (A[xmid][ymax] >= A[xmid+1][ymax]):
            return [xmid, ymax]
    elif (xmid == len(A)-1):
        if (A[xmid][ymax] >= A[xmid-1][ymax]):
            return [xmid, ymax]             
    elif (A[xmid][ymax] >= A[xmid-1][ymax]) and (A[xmid][ymax] >= A[xmid+1][ymax]):
        return [xmid,ymax]
    elif (A[xmid+1][ymax] > A[xmid][ymax]):
        return findLocalMax2D(A, xmid+1, r)
    elif (A[xmid-1][ymax] > A[xmid][ymax]):
        return findLocalMax2D(A, p, xmid-1)

#2D: brute force
def findLocalMax2DBF(A):
    global count1
    for i in range(len(A)):
        sub = A[i]
        for j in range(len(sub)):
            count1 += 1
            if (i == 0) & (j == 0):
               if (A[i][j] >= A[i+1][j]) and (A[i][j] >= A[i][j+1]):
                  return [i, j]
            elif (i == 0) & (j == len(sub)-1):
               if (A[i][j] >= A[i+1][j]) and (A[i][j] >= A[i][j-1]):
                  return [i, j]
            elif (i == len(A)-1) & (j == 0):
               if (A[i][j] >= A[i-1][j]) and (A[i][j] >= A[i][j+1]):
                  return [i, j]                                                                                    
            elif (i == len(A)-1) & (j == len(sub)-1):
               if (A[i][j] >= A[i-1][j]) and (A[i][j] >= A[i][j-1]):
                  return [i, j]
            elif (i == 0):
               if (A[i][j] >= A[i+1][j]) and (A[i][j] >= A[i][j-1]) and (A[i][j] >= A[i][j+1]):
                  return [i, j]
            elif (i == len(A)-1):
               if (A[i][j] >= A[i+1][j]) and (A[i][j] >= A[i][j-1]) and (A[i][j] >= A[i][j+1]):
                  return [i, j]
            elif (j == 0):
               if (A[i][j] >= A[i-1][j]) and (A[i][j] >= A[i+1][j]) and (A[i][j] >= A[i][j+1]):
                  return [i, j]
            elif (j == len(sub)-1):
               if (A[i][j] >= A[i-1][j]) and (A[i][j] >= A[i+1][j]) and (A[i][j] >= A[i][j-1]):
                  return [i, j]
            elif (A[i][j] >= A[i-1][j]) and (A[i][j] >= A[i+1][j]) and (A[i][j] >= A[i][j-1]) and (A[i][j] >= A[i][j+1]):
                  return [i, j]
                                                                                    
def printResult1DP4(n):
    global count0
    global count1
    count0 = 0
    count1 = 0
    lst = genList1D(n)
    time0 = time.clock()
    result0 = findLocalMax1D(lst, 0, n-1)
    time1 = time.clock()
    result1 = findLocalMax1DBF(lst)
    time2 = time.clock()

    print("Input size: ", n)
    #print("Input array: ", lst)
    print("Result: my algorithm - ", result0, ", brute force - ", result1)
    print("Loops: my algorithm - ", count0, ", brute force - ", count1)
    print("Time: my algorithm - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def test1DP4():
    print("--------------------------Problem 4 (1D cases)----------------------------")
    printResult1DP4(10)
    printResult1DP4(1000)
    printResult1DP4(100000)
    #printResult1DP4(10000000)

def printResult2DP4(n):
    global count0
    global count1
    count0 = 0
    count1 = 0
    lst = genList2D(n)
    time0 = time.clock()
    result0 = findLocalMax2D(lst, 0, n-1)
    time1 = time.clock()
    result1 = findLocalMax2DBF(lst)
    time2 = time.clock()

    print("Input size: ", n)
    #print("Input array: ", lst)
    print("Result: my algorithm - ", result0, ", brute force - ", result1)
    print("Loops: my algorithm - ", count0, ", brute force - ", count1)
    print("Time: my algorithm - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def test2DP4():
    print("--------------------------Problem 4 (2D cases)----------------------------")
    printResult2DP4(10)
    printResult2DP4(100)
    printResult2DP4(1000)
    #printResult2DP4(10000)

def main():
    testP1()
    testP2()
    testP3()
    test1DP4()
    test2DP4()

if __name__ == "__main__":
    main()
    os.system("pause")
