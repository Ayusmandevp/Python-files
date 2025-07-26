list=[4,5,6,7,2,678,-5,-123456,53,4312]
def large_find(list,idx=0):
    largest=list[idx]
    while(idx<len(list)-1):
        if largest<list[idx+1]:
            largest=list[idx+1]
        idx+=1
    return largest
def largest_remove(list,largest):
    # for element in list:
    #     if(element==largest):
    #         list.remove(element)
    list.remove(largest)

n=int(input("How many largest element you want:"))
num=1
while num<=n and list:
    print("current list:",list)
    largest=large_find(list)
    print("largest",num,"=",largest)
    largest_remove(list,largest)
    print("updated list:",list)
    num+=1