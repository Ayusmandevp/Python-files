# Polymorphism with a Function: Create a function describe_pet that takes an object of Animal and calls its speak method, demonstrating polymorphism.



class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("woof")
class Cat(Animal):
    def speak(self):
        print("Meow")
def describe_pet(animal):
    animal.speak()

dog=Dog()
cat=Cat()

describe_pet(dog)
describe_pet(cat)