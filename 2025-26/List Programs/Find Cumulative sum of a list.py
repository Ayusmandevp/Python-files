list=[1,2,3,4]
def cumulative_sum(list):
    length=len(list)
    i=0
    while i<length:
        if (i!=0):
            list[i]+=list[i-1]
        else:
            list[i]=list[i]
        i+=1
    return list
cumulativelist=cumulative_sum(list)
print("cumulative sum is",cumulativelist)