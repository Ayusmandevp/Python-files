num1,num2,num3,num4=int(input("Enter first number")),int(input("Enter second number")),int(input("Enter third number")),int(input("Enter fourth number"))
if(num1>=num2 and num1>=num3 and num1>=num4):
    print(num1,"is the greatest")
elif(num2>=num1 and num2>=num3 and num2>=num4):
    print(num2,"is the greatest")
elif(num3>=num1 and num3>=num2 and num3>=num4):
    print(num3,"is the greatest")
else:
    print(num4,"is the greatest")