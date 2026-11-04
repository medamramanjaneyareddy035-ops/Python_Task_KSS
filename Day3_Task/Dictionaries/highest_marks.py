#Write a program to find the student with the highest marks from a dictionary.
students = {
    "ram": 75,
    "ravi": 80,
    "rohit": 85
    }
topper = max(students,key=students.get)

print("Highest marks student:", topper)
print("Marks:",students[topper])
