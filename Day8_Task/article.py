#Word Counter Program 
'''A writer saves an article in a file called article.txt. Write a Python program that: 
● Opens and reads the file 
● Counts the number of words, lines, and characters in the file 
● Displays the results.
'''
f = open("article.txt","r")
data = f.read()

words = data.split()
lines = data.splitlines()
characters = len(data)

print("Number of words:",len(words))
print("Number of lines:",len(lines))
print("Number of characters:",characters)

f.close()      
