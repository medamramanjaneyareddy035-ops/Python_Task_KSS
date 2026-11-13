#Write a program to check whether a given number is a Strong number
n = int(input("Enter a number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    n = n // 10

if sum == temp:
    print(temp, "is a Strong number")
else:
    print(temp, "is not a Strong number")
