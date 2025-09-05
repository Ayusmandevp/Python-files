# Abstract Classes - Polygon Calculator: Define an abstract base class Polygon with an abstract method area. Implement this in derived classes Rectangle and Triangle.


from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(Polygon):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        print(f"Area: {self.width*self.height}")

class triangle(Polygon):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print(f"Area: {0.5*self.base*self.height}")


r1=rectangle(20,30)
r1.area()
t1=triangle(20,30)
t1.area()