class Student:
    
    # def takedata(self):
    #     name=input("Enter your name:")
    #     mark1=int(input("Enter your mark1:"))
    #     mark2=int(input("Enter your mark2:"))
    #     mark3=int(input("Enter your mark3:"))
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def getavg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("avg is",sum,self.name)
    @staticmethod
    def hello():
        print("hello hi bye")
    @staticmethod
    def hihello():
        print("hello hi bye")

s1=Student("aakash",[14,15,16])
s1.getavg()
s1.hello()
s1.hihello()