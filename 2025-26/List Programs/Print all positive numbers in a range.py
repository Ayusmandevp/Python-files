a,b=int(input("Enter the two number between which you want to find positive numbers(both numbers will be included):")),int(input())
print("The positive numbers are:\n")
for i in range(a,b+1,1):
    if i>0:
        print(i,end="\t")