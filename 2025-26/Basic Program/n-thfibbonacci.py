# n=int(input("Enter the n-th point you want to print"))
# i=0
# j=1
# count=3
# if n==1:
#     print(i)
# elif n==2:
#     print(j)
# else:
#     while count<=n:
#         new=i+j
#         i=j
#         j=new
#         if(count==n):
#             print(new,"is the",n,"idx term")
#             break
#         else:
#             count+=1

n=int(input("Enter the n-th point you want to print"))
# isfibnum=0
fiblist=[0,1,]
while True:
    fiblist.append(fiblist[-1]+fiblist[-2])
    if(len(fiblist)==n+1):
        break
print(n,"idx fibonacci number is",fiblist[n-1])
