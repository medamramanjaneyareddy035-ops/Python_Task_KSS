#6. Matrix Transformation in Image Processing 
'''An image processing system stores pixel intensity values in a matrix. 
Scenario: 
[[1, 2], 
[3, 4]] 
Task: 
● Create a NumPy array for this matrix. 
● Find its transpose. 
● Print both matrices.
'''
import numpy as np

# Create a matrix
matrix = np.array([[1,2],
                   [3,4]])

# find transpose
transpose = matrix.T

# print matrices
print("Original Matrix:")
print(matrix)

print("Transpose Matrix:")
print(transpose)
