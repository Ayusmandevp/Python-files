n=int(input("For the list,Enter the number of indexes for the list:"))
list=[]
for element in range(0,n,1):
    print("Enter the element",element+1,"for index",element)
    list.append(input())
print("Your list (before changing) is",list)
idx1,idx2=int(input("Enter the index no of one element you want to change(index 0=element 1 and so on...):")),int(input("Enter the index no of another element you want to change:"))
print("You choose",list[idx1],"and",list[idx2])
temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp
print("Your list (after changing) is",list)