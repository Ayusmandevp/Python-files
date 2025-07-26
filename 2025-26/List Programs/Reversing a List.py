# list=[1,2,3,4,5,6]
# list.reverse()
# print(list)



list=[1,2,3,4,5,6]
idx=0
while(idx<len(list)/2):
    temp=list[idx]
    list[idx]=list[len(list)-idx-1]
    list[len(list)-idx-1]=temp
    idx+=1
print("new list is:",list)