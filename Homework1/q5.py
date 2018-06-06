import math

def triangleArea(pointA, pointB, pointC):
    dAB = math.sqrt((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)
    dBC = math.sqrt((pointC[0] - pointB[0])**2 + (pointC[1] - pointB[1])**2)
    area = dAB * dBC * 0.5
    print("The area of this triangle is : ", area)
    return area

A = []
B = []
C = []

print("Please enter x coordinate for point A: ")
A.append(input())
print("Please enter y coordinate for point A: ")
A.append(input())
print("Please enter x coordinate for point B: ")
B.append(input())
print("Please enter y coordinate for point B: ")
B.append(input())
print("Please enter x coordinate for point C: ")
C.append(input())
print("Please enter x coordinate for point C: ")
C.append(input())

triangleArea(A, B, C)
