# Using Property Decorators: Implement a class Circle with a private attribute radius and use property decorators to get and set its value with checks.



class Circle:
    def __init__(self, radius=0):
        self.__radius = radius

    @property
    def radius(self):   # getter
        return self.__radius

    @radius.setter
    def radius(self, rad):   # setter
        if rad > 0:
            self.__radius = rad
        else:
            print("Radius cannot be negative")

    def area(self):
        print(f"Area: {3.14 * self.__radius ** 2}")



c1 = Circle(5)
c1.area()           
c1.radius = 8       
c1.area()           
print(c1.radius)    
