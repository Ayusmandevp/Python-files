list=[1,2,3,6,5,[],5,[],3,5,4,[],[]]
print("Your list is",list)
new=[]
for i in list:
    if i:
        new.append(i)
print(new)