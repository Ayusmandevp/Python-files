# Static and Class Methods Demonstrate the use of static and class methods in a class Calculator with methods to add and multiply numbers.

class Calculator:


    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def multiply(cls,a,b):
        return a*b
    
print("Add:",Calculator.add(5,67))
print("Multiplication:",Calculator.multiply(2,5))