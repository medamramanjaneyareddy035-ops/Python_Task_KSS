#5. Filter Values Using Condition 
'''A dataset: 
arr = np.array([10, 25, 30, 15, 40]) 
Task: 
● Convert to Pandas Series 
● Filter values greater than 20
'''
import numpy as np
import pandas as pd

arr = np.array([10, 25, 30, 15, 40])

# Covert numpy to pandas series
s = pd.Series(arr)

# filter values greater than 20
print("pandas series:")
print(s)

print("Values greater than 20:")
print(s[s > 20])
