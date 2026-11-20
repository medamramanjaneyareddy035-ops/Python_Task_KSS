#Student Result Generator (Method Overloading Concept) 
'''A school system calculates student results differently depending on available data. 
Create a Result class where a method can calculate the result using either two 
subjects or three subjects.
'''
class Result:
    def calculate(self, a, b, c=0):
        total = a + b + c
        print("Total Marks:", total)

r = Result()

r.calculate(1, 5)
r.calculate(1, 5, 6)
