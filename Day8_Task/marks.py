# Student Marks File Analyzer 
'''A teacher stores student marks in a file marks.txt in the format: 
Name Marks 
Example: 
Rahul 80 
Anita 90 
Ravi 75 
Write a Python program to: 
● Read the file 
● Display all student records 
● Calculate and display the average marks of the class
'''
f = open("marks.txt", "r")

total = 0
count = 0
print("students Records:")

for line in f:
    name,marks =line.split()

    marks = int(marks)

    print(name,marks)

    total = total + marks
    count = count + 1
average = total / count

print("average marks:",average)

f.close()
 
