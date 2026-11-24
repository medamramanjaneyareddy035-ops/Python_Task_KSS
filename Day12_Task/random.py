#8. Random Sales Simulation 
'''Scenario: 
A company wants to simulate 10 days of sales (range 100–500). 
Task: 
● Generate random integers using NumPy. 
● Print the array. 
● Find the average sales.
'''
import numpy as np

# Generate 10 random  sales values

sales = np.random.randint(100, 501, 10)

# print sales array
print("Sales for 10 days:", sales)

# Calculate average sales

average = np.mean(sales)

print("Average sales:", average)
