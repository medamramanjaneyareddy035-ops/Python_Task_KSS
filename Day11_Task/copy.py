#13. Copy vs View Behavior in Data Processing 
'''Scenario: 
A dataset: 
[10, 20, 30, 40] 
Task: 
● Create a copy of the array. 
● Modify the original array. 
● Show that the copy does not change. 
● Repeat using view() and observe the difference.
'''
import numpy as np

# Original array
arr = np.array([10, 20, 30, 40])

#  Create a copy
arr_copy = arr.copy()

# Modify original array
arr[0] = 100

print("Original array:", arr)
print("Copied array:", arr_copy)


#  Create a view
arr2 = np.array([10, 20, 30, 40])

arr_view = arr2.view()

# Modify original array
arr2[0] = 100

print("\nOriginal array:", arr2)
print("View array:", arr_view)
