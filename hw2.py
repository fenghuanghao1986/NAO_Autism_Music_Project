import pandas as pd
import numpy as np
# Q2
SD = pd.read_csv('DMHomeworkSalesData.csv', skiprows=[0], \
                 names=['Month', 'Sales', 'Location', \
                        'Amount', 'Coupon'])
SDF = pd.DataFrame(SD)
# Q3
print(SDF)
# Q4
SDF.loc[[2],"Sales":"Coupon"] = [32, 'Parker', 23000, 29]
print(SDF)
# Q5
SDF.index = SDF.Month
SDF.drop(SDF.columns[[0]], axis=1, inplace=True)
print(SDF)
# Q6
max(SDF.Sales)

