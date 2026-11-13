#Write a program to check whether a given number is an Armstrong number or not.
n = int(input("Enter a number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10

if sum == temp:
    print(temp, "is an Armstrong number")
else:
    print(temp, "is not an Armstrong number")
