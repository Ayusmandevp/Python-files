class Student:
    college_name="CUAP"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def welcome(self):
        print("Hello")
        print("Name and roll no is",self.name,self.roll)
    def getmark(self):
        return self.roll*10
s1=Student("Ayusman",13)
s1.welcome()
print(s1.getmark())
