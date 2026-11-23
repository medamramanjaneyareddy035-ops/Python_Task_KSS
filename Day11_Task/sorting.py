#12. Sorting Customer Names 
'''A system stores customer names: 
["Ravi", "Anil", "Sita", "John"] 
Task: 
● Convert it to a NumPy array. 
● Sort the names alphabetically.
'''
import numpy as np

names = ["Ravi", "Anil", "Sita", "John"]

arr = np.array(names)

sorted_names = np.sort(arr)

print("Original Names:")
print(arr)

print("Sorted Names:")
print(sorted_names)
