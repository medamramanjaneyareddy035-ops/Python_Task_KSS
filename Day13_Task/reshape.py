#5. Reshape & Row Averages 
'''A dataset: 
data = np.arange(1, 13) 
Task: 
● Reshape it into a 3×4 matrix 
● Compute average of each row
'''
import numpy as np

# Create array from 1 to 12
data = np.arange(1, 13)

# Reshape it into a 3x4 matrix
matrix = data.reshape(3, 4)

print("3x4 Matrix:")
print(matrix)

# Calculate row averages
row_avg = np.mean(matrix, axis=1)

print("Row Averages:", row_avg)
