#Write a program to check whether a string is a palindrome.
name = input("Enter a string: ")

if name == name[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
