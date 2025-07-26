class student:
    def __init__(self):
        self.name=input("Enter your name:")
        self.roll=int(input("Enter your roll no:"))
        self.mark1=int(input("Enter your mark1:"))
        self.mark2=int(input("Enter your mark2:"))
        self.mark3=int(input("Enter your mark3:"))

    def printdata(self):
        print("name is:",self.name)
        print("roll no is",self.roll)
        print("your marks are",self.mark1,self.mark2,self.mark3)

s1=student()
s2=student()
s1.printdata()
s2.printdata()