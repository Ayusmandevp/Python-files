# Last Digit in Words: Write a class with a method that takes an integer and prints the last digit of that number in words.

class Number:
    def __init__(self,num):
        self.num=num
        self.digit=self.num%10
    def digitLetter(self):
        lettterDict={1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",0:"ZERO"}
        print(f"last digit is {lettterDict[self.digit]}")

n1=Number(345)
n1.digitLetter()
n2=Number(3475468)
n2.digitLetter()