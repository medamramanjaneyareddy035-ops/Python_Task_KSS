#  Write a Python program that generates 20 random numbers between 1 and 200 using 
'''the random module and store them in a list. 
Then using the math module, compute and display: 
● Maximum value 
● Minimum value 
● Square root of the maximum number
'''
import random
import math

# Generate 20 random numbers between 1 and 200
numbers = []

for i in range(20):
    numbers.append(random.randint(1, 200))

# Display the list
print("Random Numbers:", numbers)

# Find maximum and minimum values
maximum = max(numbers)
minimum = min(numbers)

# Calculate square root of maximum number
sqrt_max = math.sqrt(maximum)

# Display the results
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
print("Square Root of Maximum Number:", sqrt_max)
