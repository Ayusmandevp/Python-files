# Exercise 6: Design a Rectangle class with default attributes for length and width set to 1. Include methods to set these attributes and calculate the area.

class Rectangle:
    def __init__(self,length=1,width=1):
        self.length=length
        self.width=width
    def set_value(self,len,wid):
        self.length=len
        self.width=wid
    def get_area(self):
        print("Area is",self.length*self.width)
r1=Rectangle()
r1.get_area()
r1.set_value(4,5)
r1.get_area()