#Write a program to count the number of vowels in a string.
name = input("Enter a string: ")

count = 0

for ch in name:
    if ch in "aeiouAEIOU":
        count += 1
print("number of vowels:",count)        
