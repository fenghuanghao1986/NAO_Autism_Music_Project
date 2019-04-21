#Zimian Li
#Q2
import random
import time

count0 = 0
count1 = 0

def genList(n):
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
        
    
def printResult(n):
    global count0
    global count1
    count0 = 0
    count1 = 0
    lst = genList(n)
    time0 = time.clock()
    result0 = findBoundingBoxDAC(lst, 0, n-1)
    time1 = time.clock()
    result1 = findBoundingBoxBF(lst)
    time2 = time.clock()

    print("Input size: ", n)
    print("Result: DAC - ", result0, ", brute force - ", result1)
    print("Comparisonss: DAC - ", count0, ", brute force - ", count1)
    print("Time: DAC - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def test():
    print("Problem 2:")
    printResult(10)
    printResult(1000)
    printResult(100000)
    printResult(100001)
    #printResult(10000000)
    
