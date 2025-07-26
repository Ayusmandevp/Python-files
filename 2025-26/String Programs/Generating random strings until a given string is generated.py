import random
import string

values=string.ascii_letters+string.digits+string.punctuation+string.whitespace
# values=string.ascii_letters


def stringoflength(str,values):
    word=""
    for i in range(0,len(str),1):
        word+=random.choice(values)
    return word
count=0
str=input("Enter the string:")
while True:
    generating=stringoflength(str,values)
    count+=1
    if(generating==str):
        break
print(str,"generated after",count,"times")

