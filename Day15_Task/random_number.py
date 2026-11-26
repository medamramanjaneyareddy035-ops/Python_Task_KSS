#2. Random Number Analyzer 
'''Scenario: 
A system generates random numbers for testing. 
Task: 
● Use random to generate 10 numbers 
● Store in a list 
● Use loop + condition to count even/odd numbers 
● Use set to remove duplicates
'''
import random

# Generate 10 random numbers
numbers = []

for i in range(10):
    num = random.randint(1, 100)
    numbers.append(num)

print("Random Numbers:")
print(numbers)

# Count even and odd numbers
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nEven Numbers Count:", even_count)
print("Odd Numbers Count:", odd_count)

# Remove duplicates using set
unique_numbers = set(numbers)

print("\nUnique Numbers:")
print(unique_numbers)
