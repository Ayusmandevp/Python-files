#  Student Grade Calculator: Implement a Student class with attributes for name and a list of marks. Include a method to calculate the average and determine the grade.
from functools import reduce
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(f"Hello {self.name}")
    def average(self):
        self.total=reduce(lambda x,y:x+y,self.marks)
        self.avg=self.total/len(self.marks)
        print(f"Average is {self.avg}")
    def  grade(self):
        if self.avg>90:
            print("Grade: A+")
        elif self.avg>80:
            print("Grade: A")
        elif self.avg>70:
            print("Grade: B+")
        elif self.avg>60:
            print("Grade: B")
        elif self.avg>30:
            print("Grade: Pass")
        else:
            print("FAIL")

s1=Student("Ayusman",[94,97,89,98,85])
s1.average()
s1.grade()