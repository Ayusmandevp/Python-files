# Person Class with __str__ Method: Create a Person class with first and last name attributes and override the __str__ method to return the full name.

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def __str__(self):
        return f"{self.fname} {self.lname}"

n=Person("Ayusman","Satapathy")
print(n)