import math

def equation(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(delta))/(2 * a)
    x2 = (-b - math.sqrt(delta))/(2 * a)
    print("The first solution is: x1 = ", x1)
    print("The second solution is : x2 = ", x2)
    return

print("Test equation is like x**2 + 3*x - 4 = 0")
a = 1
b = 3
c = -4
print("Here are the result: ")
equation(a, b, c)
