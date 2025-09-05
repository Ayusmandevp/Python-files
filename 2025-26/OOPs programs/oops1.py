#Exercise 1: Create a class Greeter with a method greet(name) that prints a greeting for the provided name.



#method 1


# class Greeter:
#     def __init__(self):
#         self.name=input("Enter Your name:")
#     def greet(self):
#         print("Hello",self.name)


# g1=Greeter()
# g1.greet()


# method 2



class Greeter:
    def greet(self,name):
        print("Hello",name)

g1=Greeter()
g1.greet("Ayusman")