#Write a program to assign grades based on marks (for example: A, B, C, Fail).

marks = int(input("Enter your marks:"))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("fail")
