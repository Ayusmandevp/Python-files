age=int(input("enter your age:"))
print("Your age is",age)
if(age<13):
    print("You are child.\n You can not vote")
elif(age<18):
    print("You are teenager.\n You can not vote")
else:
    print("You are an adult.\n You can vote")