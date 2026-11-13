#Write a program to check whether a number is Prime.
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Factors = 1,", n)
    print(n, "is a Prime number")
else:
    print(n, "is not a Prime number")
