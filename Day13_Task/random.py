#8. Random Data & Filtering 
'''Generate random numbers: 
nums = np.random.randint(1, 100, 10) 
Task: 
● Filter values that are divisible by 5 
● Return sorted result.
'''
import numpy as np

# Generate 10 random numbers
nums = np.random.randint(1, 100, 10)

print("Original Numbers:", nums)

# Filter numbers divisible by 5
filtered = nums[nums % 5 == 0]

# Sort the filtered numbers
result = np.sort(filtered)

print("Numbers Divisible by 5:", filtered)
print("Sorted Result:", result)
