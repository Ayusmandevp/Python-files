sum=0
addornot="y"
print("Welcome to addition calculator")
while(True):
    num=int(input("Enter the number to add in sequence:"))
    sum+=num
    addornot=input("Do you want to add number if yes then press 'y' or else 'n'")
    if(addornot =='n' or addornot=='N'):
        break
    elif(addornot =="y" or addornot=="Y"):
        continue
    else:
        print("i am not getting you , wanna continue...")
print("sum is",sum)