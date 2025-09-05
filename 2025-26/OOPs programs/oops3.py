# Exercise 3: Build a class Employee with multiple constructors that can initialize an employee object in different ways.


class Employee:
    def __init__(self,name,id=None,dept=None):
        self.name=name
        self.id=id
        self.dept=dept
    def printvalue(self):
        print(f"name: {self.name}")
        if self.id:
            print(f"id: {self.id}")
        if self.dept:
            print(f"dept: {self.dept}")


e1=Employee("Ayusman")
e1.printvalue()
e2=Employee("omm",456)
e2.printvalue()
e3=Employee("liku",234,"cs")
e3.printvalue()