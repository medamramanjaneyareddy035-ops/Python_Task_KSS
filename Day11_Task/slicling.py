#4. Student Roll Numbers Extraction 
'''A list contains roll numbers: 
[101, 102, 103, 104, 105, 106] 
Scenario: 
You want only the middle students (index 2 to 4). 
Task: 
● Use NumPy slicing to extract those values.
'''
import numpy as np

roll_numbers = [101, 102, 103, 104, 105, 106]

arr = np.array(roll_numbers)

print(arr)
print("Middle students:", arr[2:5])
