list=[1,2,3,4,5,6,7,8,9,10]
print("Your list (before changing) is",list)
temp=list[0]
list[0]=list[-1]
list[-1]=temp
print("Your list (after changing) is",list)
