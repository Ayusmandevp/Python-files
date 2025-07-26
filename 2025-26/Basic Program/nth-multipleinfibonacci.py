# n=int(input("Enter the n-th point you want to print"))
mul=int(input("Enter the number whose multiple you want to see"))
print("You want to see the number multiply by",mul,"before any particular number or you want some number of them?")
print("if you want till any number press 'A' or 'a' or if you want some no of them enter 'B' or 'b'")
choice=str(input("Your choice:"))
if choice=='a' or choice=='A':
    n=int(input("Enter the number:"))
    fiblist=[0,1,]
    while True:
        fiblist.append(fiblist[-1]+fiblist[-2])
        if(fiblist[-1]>=n):
            break
    for nums in fiblist:
        if(nums%mul==0):
            print(nums)
elif choice=='b' or choice=='B':
    n=int(input("Enter the number of fibonacci elements:"))
    fiblist=[0,1,]
    while True:
        fiblist.append(fiblist[-1]+fiblist[-2])
        count=0
        for nums in fiblist:
            if(nums%mul==0):
                print(nums)
                count+=1
        if(count==n):
            break
else:
    print("invalid input")