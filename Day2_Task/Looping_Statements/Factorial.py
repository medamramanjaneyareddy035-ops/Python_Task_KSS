#Write a program to calculate the factorial of a number using a loop.

num = int(input("Enter a number:"))
fact = 1

if num <0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range (1, num + 1):
        fact =fact*1
print("Factorial:",fact)   
