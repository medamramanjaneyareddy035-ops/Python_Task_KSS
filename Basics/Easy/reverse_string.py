#String Reversal: Write a program to reverse a string without using built-in reverse functions.

name = input("Enter a string: ")

reverse = ""

for ch in name:
    reverse = ch + reverse

print("Reversed string:",reverse)    
