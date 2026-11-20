#Rectangle Area Calculator (Constructor) 
'''A geometry application needs to calculate the area of rectangles. Create a Rectangle 
class that uses a constructor to initialize length and width. Add a method to calculate 
and display the area. 
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        print("Area of Rectangle:", result)


r = Rectangle(2, 4)
r.area()
