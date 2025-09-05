# Exercise 2: Develop a class Calculator with methods to add and subtract two numbers.

class Calculator:
    def add(self,num1,num2):
        print("Sum is",num1+num2)
    def substract(self,num1,num2):
        print("Sub is",num1-num2)
n1=Calculator()
n1.add(1,3)
n1.substract(5,4)