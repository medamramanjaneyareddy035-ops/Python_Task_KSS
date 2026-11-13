#Write a program to check whether a number is a Palindrome.
n = int(input("Enter a number: "))
temp = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if reverse == temp:
    print(temp, "is a Palindrome number")
else:
    print(temp, "is not a Palindrome number")
