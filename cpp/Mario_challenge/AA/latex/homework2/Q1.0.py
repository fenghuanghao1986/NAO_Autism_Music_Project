#Zimian Li
#Q1
import random

count = 0

def genSortedList(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(240,360))
    lst.sort()
    return lst

def findUpper(A, x, p, r):
    global count
    count += 1
    mid = (p+r)//2
    if (A[mid] != x) & ((p == r) | (mid == 0) | (mid == len(A)-1)):
        return None
    elif (A[mid] == x) & ((p == r) | (mid == 0) | (mid == len(A)-1)):
        return mid
    elif(A[mid] == x) & (A[mid+1] > A[mid]):
        return mid
    elif A[mid] > x:
        return findUpper(A, x, p, mid-1)
    elif (A[mid] < x) | ((A[mid] == x) & (A[mid+1] == x)):
        return findUpper(A, x, mid+1, r)

def findLower(A, x, p, r):
    global count
    count += 1
    mid = (p+r)//2
    if (A[mid] != x) & ((p == r) | (mid == 0) | (mid == len(A)-1)):
        return None
    elif (A[mid] == x) & ((p == r) | (mid == 0) | (mid == len(A)-1)):
        return mid
    elif (A[mid] == x) & (A[mid-1] < A[mid]):
        return mid
    elif (A[mid] > x) | ((A[mid] == x) & (A[mid-1] == x)):
        return findLower(A, x, p, mid-1)
    elif A[mid] < x :
        return findLower(A, x, mid+1, r)

def countScore(A, x):
    i = findUpper(A, x, 0, len(A)-1)
    if i == None:
        return None
    j = findLower(A, x, 0, len(A)-1)
    return i-j+1

def printResult(n, x):
    global count
    count = 0
    lst = genSortedList(n)
    num = countScore(lst, x)
    print("Number of score ",x,": ", num, ", Comparisons: ", count)
