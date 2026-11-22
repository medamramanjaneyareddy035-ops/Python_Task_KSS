#5. Store Sales Comparison 
'''Two stores record daily sales for 3 days. 
Scenario: 
Store A = [200, 250, 300] 
Store B = [180, 270, 310] 
Task: 
● Store them in NumPy arrays. 
● Find the daily difference in sales between the two stores. 
● Print the resulting array.
'''
import numpy as np

# store sales
store_a = np.array([200, 250, 300])
store_b = np.array([180, 270, 310])

# Find daily differnce
differnce = store_a - store_b

# print  results
print("store A sales:",store_a)
print("store B sales:",store_b)
print("Differnce:",differnce)
