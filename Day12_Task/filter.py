#7. Filter Positive Even Numbers from Dataset 
'''Scenario: 
A dataset contains mixed values: 
arr = [-5, 10, 15, -2, 20, 25, 30] 
Task: 
● Convert to NumPy array. 
● Filter values that are: 
○ Positive 
○ Even
'''
import numpy as np

arr = [-5, 10, 15, -2, 20, 25, 30]

# Convert list into numpy array

r = np.array(arr)

# Filter positive even numbers

result =r[(r > 0) & (r % 2 == 0)]

print("Original Array:", r)
print("Postive even numbers:", result)
