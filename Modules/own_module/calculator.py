#Create a Python module named calculator.py that contains functions to perform: 
'''● Addition 
● Subtraction 
● Multiplication 
● Division 
Then write another Python program that imports this module and performs calculations 
based on user input.
'''
# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not possible."
import calculator

# Get input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result:", calculator.add(a, b))

elif choice == 2:
    print("Result:", calculator.subtract(a, b))

elif choice == 3:
    print("Result:", calculator.multiply(a, b))

elif choice == 4:
    print("Result:", calculator.divide(a, b))

else:
    print("Invalid choice!")    
