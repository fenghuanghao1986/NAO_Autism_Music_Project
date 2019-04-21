#Zimian Li
#Q4
import random
import time

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
    #others
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
                                                                                    
def printResult1D(n):
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
    print("Result: my algorithm - ", result0, ", brute force - ", result1)
    print("Loops: my algorithm - ", count0, ", brute force - ", count1)
    print("Time: my algorithm - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def test1D():
    printResult1D(10)
    printResult1D(1000)
    printResult1D(100000)
    #printResult1D(10000000)

def printResult2D(n):
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
    print("Result: my algorithm - ", result0, ", brute force - ", result1)
    print("Loops: my algorithm - ", count0, ", brute force - ", count1)
    print("Time: my algorithm - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def test2D():
    printResult2D(10)
    printResult2D(100)
    printResult2D(1000)
    #printResult2D(10000)
