a,b=int(input("Enter the two number between which you want to find even numbers(both numbers will be included):")),int(input())
print("The even numbers are:\n")
for i in range(a,b+1,1):
    if i%2==0:
        print(i,end="\t")