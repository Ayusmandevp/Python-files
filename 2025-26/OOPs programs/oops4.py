# Exercise 4: Design a class SeriesCalculator that calculates the sum of an arithmetic series.
from functools import reduce

class SeriesCalculator:
    def __init__(self):
        self.list_series=[int(x) for x in input("Enter the elements of the series ,separated by ','").split(",")]
        print(f"sum is {reduce(lambda x,y:x+y,self.list_series)}")

e1=SeriesCalculator()