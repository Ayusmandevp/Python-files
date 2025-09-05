# Exercise 13: Car Class: Create a Car class with attributes make, model, and year. Include a method to display the details of the car.

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(f"make: {self.make}, model: {self.model}, year= {self.year}")


c1=Car("Toyota","Corolla",2021)
c1.display()