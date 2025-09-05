# Exercise 5: Create a class MaxFinder that identifies the largest number in a list.
from functools import reduce

class MaxFinder:
    def __init__(self,list):
        self.list=list
        print(f"largest is {reduce(lambda x,y:x if x>y else y,self.list)}")


f1=MaxFinder([1,5,8,3,9,2])