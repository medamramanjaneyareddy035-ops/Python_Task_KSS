# Write a Python program using the math module to calculate and display the square root, floor value, and ceiling value of a number entered by the user. 
import math

num = float(input("Enter a number: "))

if num >= 0:
    print("Square root:", math.sqrt(num))
else:
    print("Square root is not defined for negative numbers.")

print("Floor value:", math.floor(num))
print("Ceiling value:", math.ceil(num))
