# Q1

import pandas as pd
import numpy as np

print("Q1")
IceCream = pd.read_csv('DML2IceCreamData.csv')
print(IceCream.head(15))

# Q2
print("Q2")
IceCream.drop(IceCream.columns[[0]], axis=1, inplace=True)
print(IceCream.head(15))

# Q3
print("Q3")
IceCream.Sales.fillna(IceCream.groupby('Type') \
                      .Sales.transform('median'), inplace=True)
print(IceCream.head(15))

# Q4
print("Q4")
goalCol = np.zeros((), dtype=int)
IceCream.insert(loc=5, column='Goal', value=goalCol)
print(IceCream.head(15))

# Q5
print("Q5")
StoreData = pd.read_csv('DML2StoreData.csv')
print(StoreData)

# Q6
print("Q6")
j = len(StoreData.Goal)
for i in range(j):
    mask = IceCream.Store == StoreData.Store[i]
    column_name = 'Goal'
    IceCream.loc[mask, column_name] = StoreData.Goal[i]
print(IceCream.head(15))

# Q7
print("Q7")
IceCream.to_csv('EmmaLiuDML2ICData.csv')

# Q8
print("Q8")
aveAge = IceCream.Age.mean()
aveSales = IceCream.Sales.mean()
aveGoal= IceCream.Goal.mean()
aveAll = {"Age": [aveAge], "Sales": [aveSales], "Goal": [aveGoal]}
AverageDataFrame = pd.DataFrame(aveAll)
AverageDataFrame.set_index([['Average']], inplace=True)
print(AverageDataFrame)

# Q9
print("Q9")

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Greeley'
b = IceCream.iloc[:, 2]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveGreeAge = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Greeley'
b = IceCream.iloc[:, 3]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveGreeSales = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Greeley'
b = IceCream.iloc[:, 5]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveGreeGoals = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Denver'
b = IceCream.iloc[:, 2]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveDenAge = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Denver'
b = IceCream.iloc[:, 3]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveDenSales = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Denver'
b = IceCream.iloc[:, 5]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveDenGoals = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Parker'
b = IceCream.iloc[:, 2]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveParAge = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Parker'
b = IceCream.iloc[:, 3]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveParSales = np.mean(greeleyAge)

a = IceCream.iloc[:, 4]
a = np.array(a)
boolList = a == 'Parker'
b = IceCream.iloc[:, 5]
greeleyAge = np.array(b)
greeleyAge = greeleyAge[boolList]
aveParGoals = np.mean(greeleyAge)

AgeSalesGoals = {"Greeley": [aveGreeAge, aveGreeSales, aveGreeGoals], \
                 "Denver": [aveDenAge, aveDenSales, aveDenGoals], \
                 "Parker": [aveParAge, aveParSales, aveParGoals]}
ASG = pd.DataFrame(AgeSalesGoals)
ASG.set_index([['Age', 'Sales', 'Goals']], inplace=True)
print(ASG)

# New version of Q9
print("Q9")
k = len(IceCream.Type)

# Average Age Loop
greAge = []
parAge = []
denAge = []
for l in range(k):
    if IceCream.Store[l] == StoreData.Store[0]:
        greAge.append(IceCream.Age[l])
    elif IceCream.Store[l] == StoreData.Store[1]:
        parAge.append(IceCream.Age[l])
    elif IceCream.Store[l] == StoreData.Store[2]:
        denAge.append(IceCream.Age[l])
greAveAge = np.mean(greAge)
parAveAge = np.mean(parAge)
denAveAge = np.mean(denAge)

# Average Sales Loop
greSales = []
parSales = []
denSales = []
for l in range(k):
    if IceCream.Store[l] == StoreData.Store[0]:
        greSales.append(IceCream.Sales[l])
    elif IceCream.Store[l] == StoreData.Store[1]:
        parSales.append(IceCream.Sales[l])
    elif IceCream.Store[l] == StoreData.Store[2]:
        denSales.append(IceCream.Sales[l])
greAveSales = np.mean(greSales)
parAveSales = np.mean(parSales)
denAveSales = np.mean(denSales)

# Average Goal Loop
greGoal = []
parGoal = []
denGoal = []
for l in range(k):
    if IceCream.Store[l] == StoreData.Store[0]:
        greGoal.append(IceCream.Goal[l])
    elif IceCream.Store[l] == StoreData.Store[1]:
        parGoal.append(IceCream.Goal[l])
    elif IceCream.Store[l] == StoreData.Store[2]:
        denGoal.append(IceCream.Goal[l])
greAveGoal = np.mean(greGoal)
parAveGoal = np.mean(parGoal)
denAveGoal = np.mean(denGoal)
# Creating dataframe from Dic
ASG = {"Greeley": [greAveAge, greAveSales, greAveGoal], \
       "Denver": [denAveAge, denAveSales, denAveGoal], \
       "Parker": [parAveAge, parAveSales, parAveGoal]}
AgeSalesGoals = pd.DataFrame(ASG)
AgeSalesGoals.set_index([['Age', 'Sales', 'Goals']], inplace=True)
print(AgeSalesGoals)