#Import the modules from the utilities package and use their functions.
from utilities import math_operations
from utilities import string_operations

# Mathematical operations
a = 10
b = 5

print("Addition:", math_operations.add(a, b))
print("Multiplication:", math_operations.multiply(a, b))

# String operations
text = "Hello Python"

print("Uppercase:", string_operations.to_uppercase(text))
print("Character Count:", string_operations.count_characters(text))
