#Write a program to check whether a substring exists in a string.

name = input("Enter a string: ")

sub = input("Enter a substring: ")

if sub in name:
    print("substring exists")
else:
    print("does not exists")
