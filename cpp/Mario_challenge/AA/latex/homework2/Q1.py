#Zimian Li
#Q1
import random
import time

count0 = 0
count1 = 0

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

#My algorithm
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

def printResult(n):
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
    #print("Result: my algorithm - ", result0, ", brute force - ", result1)
    print("Loops: my algorithm - ", count0, ", brute force - ", count1)
    print("Time: my algorithm - ", round(1000*(time1-time0),5),"ms", ", brute force - ", round(1000*(time2-time1),5),"ms")
    print("--------------------------------------------------------------------------")

def test():
    print("Problem 1:")
    printResult(10)
    printResult(1000)
    printResult(100000)
    printResult(10000000)
