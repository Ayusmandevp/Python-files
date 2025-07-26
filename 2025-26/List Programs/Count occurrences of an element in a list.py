list=[1,2,3,4,5,4,3,3,2,6,1]
count=0
num=int(input("Enter the number whose occurence you want to check:"))
for i in list:
    if(i==num):
        count+=1
print("The element",num,"is present for",count,"times.")