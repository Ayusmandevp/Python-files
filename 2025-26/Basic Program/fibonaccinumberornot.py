n=int(input("Enter the number:"))
isfibnum=0
fiblist=[0,1,]
while True:
    fiblist.append(fiblist[-1]+fiblist[-2])
    if(fiblist[-1]+fiblist[-2]>n):
        break
for fibnums in fiblist:
    if(fibnums==n):
        isfibnum=1
        # break
    else:
        isfibnum=0
if(isfibnum==1):
    print(n,"is a fibbonacci number")
else:
    print(n,"is not a fibbonacci number")