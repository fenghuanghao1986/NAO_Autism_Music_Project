# Question 3

# Part A
import pandas as pd
import numpy as np

print("Part A")
carPrice = {'Manufacturer': ['Honda', 'Nissan', 'Toyota', 'Honda', \
                             'Toyota', 'Ford', 'Hyundai', 'Hyundai', \
                             'Toyota', 'Chevrolet', 'Chevrolet', \
                             'Nissan', 'Ford', 'Volkswagon', 'Chevrolet'],
            'Model': ['Accord', 'Altima', 'Camry', 'Civic', 'Corolla', \
                      'Fusion', 'Sonata', 'Elantra', 'Prius', 'Cruze', \
                      'Impala', 'Sentra', 'Focus', 'Jetta', 'Malibu'],
            'Sales2011': [33616, 32289, 31464, 31213, 30234, 27566, \
                          22894, 19255, 18605, 18101, 18063, 17851, \
                          17178, 16969, 15551],
            'Sales2010': [29120, 24649, 36251, 22463, 29623, 22773, \
                          18935, 8225, 11786, 10316, 15594, 8721, \
                          19500, 9196, 17750]}
MyData = pd.DataFrame(carPrice)
MyData.index = MyData.index + 1
print(MyData)

# Part B
print("Part B")
print(MyData.iloc[0: 10])

# Part C
print("Part C")
print(MyData.iloc[-3::])

# Part D
print("Part D")
print(MyData.iloc[:, 0])

# Part E
print("Part E")
print(MyData.iloc[:, 1::])

# Part F
print("Part F")
print(MyData.iloc[4:10])

# Part G
print("Part G")
print(MyData.iloc[[4,5,6,7,8,9],[1,2]])

# Part H
print("Part H")
MyData = MyData.rename(columns = {'Manufacturer': 'Producer'})
print(MyData.iloc[0:4])

# Part I
print("Part I")
Sales2012 = np.array([MyData.iloc[:, 3] + 1000]).T
MyData.insert(loc=4, column='Sales2012', value=Sales2012)
print(MyData.head(5))

# Part J
print("Part J")
MyData.drop(MyData.columns[[2]], axis=1, inplace=True)
print(MyData.head(5))

# Part K
print("Part K")
MyData.set_index([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', \
                  'L', 'M', 'N', 'O']], inplace=True)
print(MyData.head(5))

# Part L
print("Part L")
print(MyData.loc[MyData['Producer'] == 'Toyota'])

# Part M
print("Part M")
print(MyData.loc[MyData['Sales2011'] > 20000])
