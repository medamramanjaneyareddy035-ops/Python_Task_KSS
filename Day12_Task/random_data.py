#12. Random Dataset Normalization + Filtering 
'''Scenario: 
● Generate 8 random float values between 0 and 1. 
Task: 
1. Normalize by multiplying with 100 
2. Filter values greater than 50 
3. Sort the filtered values
'''
import numpy as np

# Generate 8 random float values
arr = np.random.rand(8)

print("Original values:", arr)

# Normalize by multiplying with 100
normalized = arr * 100

print("Normlized values:", normalized)

# Filter values greater than 50
filtered = normalized[normalized > 50]

print("Filtered values:", filtered)

#sort filtered values

sorted_values = np.sort(filtered)
print("Sorted values:", sorted_values)
