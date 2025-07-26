list=[1,2,3,4,5,6,7,8,9,10]
chunklist=[]
limit=0
i=0
while i<len(list):
    newlist=[]
    while i<limit+3:
        if i<len(list):
            newlist.append(list[i])
        i+=1
    chunklist.append(newlist)
    limit+=3
print(chunklist)