# Write a Python program with a function that returns the largest of three numbers.
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


x = int(input("Enter first number: "))

y = int(input("Enter second number: "))

z = int(input("Enter third number: "))

result = largest(x, y, z)

print("Largest number is:", result)
