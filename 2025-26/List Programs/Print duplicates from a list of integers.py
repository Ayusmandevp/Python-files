list=[1,2,3,4,3,2,1,5,5,8]
duplicate=set()
for i in list:
    count=0
    for j in list:
        if i==j:
            count+=1

    if count>=2:
        duplicate.add(i)
print("duplicate numbers are",duplicate)     