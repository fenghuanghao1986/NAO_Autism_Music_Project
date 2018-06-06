# Question 2

# Part A
import numpy as np
import pandas as pd

print("Part A")
Scales_List = [135, 145, 175, 180, 160, 135, 210, 175, 160, 120, 115, 120]
MyArray = np.array(Scales_List)
print(MyArray)

# Part B
print("Part B")
boolList = MyArray > 150
greater150 = MyArray[boolList]
print(greater150)

# Part C
print("Part C")
print(np.shape(MyArray))
print(len(MyArray))
print(MyArray.size)
print(MyArray.shape)

# Part D
print("Part D")
MySeries = pd.Series(MyArray)
print(MySeries)

# Part E
print("Part E")
MySeries1 = pd.Series(MyArray, index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
print(MySeries1)
