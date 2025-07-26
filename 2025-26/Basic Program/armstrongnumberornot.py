num=int(input("Enter the number to be checked:"))
numcopy=num
digitno=0
powersum=0
while numcopy>0:
    # digit=numcopy%10
    numcopy//=10
    digitno+=1
print("total no of digit",digitno)
numcopy=num #reset the numcopy
while numcopy>0:
    digit=numcopy%10
    powersum+=digit**digitno
    numcopy//=10
if (powersum==num):
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")