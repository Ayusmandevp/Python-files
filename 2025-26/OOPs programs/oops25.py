# Managing Private Attributes Create a Person class with private attributes name and age and provide getter and setter methods to manage these attributes safely.

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @property
    def access_value(self):
        return f"name: {self.__name}  age: {self.__age}"
    
    @access_value.setter
    def access_value(self,data):
        self.__name=data[0]
        self.__age=data[1]


p1=Person("Purnima",22)
print(p1.access_value)    
p1.access_value=("Purnima Routray",27)
print(p1.access_value)    
