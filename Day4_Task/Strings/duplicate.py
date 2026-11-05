# Write a program to remove duplicate characters from a string.
name = input("Enter a string: ")

result = ""

for ch in name:
     if ch not in result:
         result += ch
print("After removing duplicates:",result)        
         
