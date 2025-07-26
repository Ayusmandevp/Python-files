list=[4,5,6,7,2,678,-5,-123456,53,4312]
def largest(list,idx=0):
    largest=list[idx]
    while(idx<len(list)-1):
        if largest<list[idx+1]:
            largest=list[idx+1]
        idx+=1
    return largest
def largest_remove(list,largest):
    for element in list:
        if(element==largest):
            list.remove(element)
largest1=largest(list)
largest_remove(list,largest1)
print(list)
largest2=largest(list)
print("second largest is",largest2)