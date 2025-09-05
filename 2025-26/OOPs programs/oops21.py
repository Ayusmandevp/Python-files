# Interface Implementation Create an interface Shape with methods area() and perimeter(). Implement this interface in Rectangle and Circle classes.

from abc import ABC, abstractmethod



class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def perimeter(self):
        return 2*(self.width+self.height)
    def area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def perimeter(self):
        return 2*3.14*self.radius

    def area(self):
        return 3.14*self.radius**2
    

r1=Rectangle(2,4)
print("Rectangle perimeter:",r1.perimeter())
print("Rectangle area:",r1.area())

c1=Circle(2)
print("Circle perimeter:",c1.perimeter())
print("Circle area:",c1.area())