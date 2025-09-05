# Calculating Student Results: Develop a class to accept a student's name and marks in three subjects, then calculate and display the total and average marks.


class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def totalavg(self):
        print(f"Total= {self.mark1+self.mark2+self.mark3} and Average= {(self.mark1+self.mark2+self.mark3)/3}")

s1=Student("Ankit",89,67,90)
s1.totalavg()