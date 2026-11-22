#7. Splitting Data for Parallel Processing 
'''A dataset contains the following values: 
[5, 10, 15, 20, 25, 30] 
Scenario: 
You want to distribute the data across 3 processors. 
Task: 
● Store the data in a NumPy array. 
● Split it into 3 equal parts using NumPy.
'''
import numpy as np
# Create an array
data = np.array([5, 10, 15, 20, 25, 30])

# split into 3 equal parts
result = np.split(data, 3)

#print result
print("Original Array:", data)
print("Split Arrays:", result)
