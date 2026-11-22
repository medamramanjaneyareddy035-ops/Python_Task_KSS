#10. Data Processing Pipeline 
'''A data pipeline receives the following array: 
[12, 7, 25, 3, 18, 10] 
Scenario: 
1. Convert the list into a NumPy array. 
2. Sort the array. 
3. Split the sorted array into two equal parts. 
4. Calculate the sum of each part. 
Output: 
● Sorted array 
● Two split arrays 
● Sum of each part
'''
import numpy as np

# 1. Convert list into NumPy array
data = [12, 7, 25, 3, 18, 10]
arr = np.array(data)

# 2. Sort the array
sorted_arr = np.sort(arr)

# 3. Split the sorted array into two equal parts
part1, part2 = np.split(sorted_arr, 2)

# 4. Calculate the sum of each part
sum1 = np.sum(part1)
sum2 = np.sum(part2)

# Print results
print("Sorted Array:", sorted_arr)
print("First Split Array:", part1)
print("Second Split Array:", part2)
print("Sum of First Part:", sum1)
print("Sum of Second Part:", sum2)
