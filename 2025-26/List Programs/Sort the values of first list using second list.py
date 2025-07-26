baselist=["apple",'banana',"cherry","chicoo"]
sortlist=[2,3,10,4]


def list_copy(list):

    listcopy=[]
    for i in range(0,len(list),1):
        listcopy.append(list[i])
    return listcopy
        

def index_sorting(sortlist,mainlist,baselist):
    sortedbaselist=[]
    for i in sortlist:
        idx=mainlist.index(i)
        sortedbaselist.append(baselist[idx])
    return sortedbaselist


sortlistcopy=list_copy(sortlist)
sortlistcopy.sort(reverse=True)
sortedbaselist=index_sorting(sortlistcopy,sortlist,baselist)
print("Your sorted baselist in precedence of sort list's descending order is:",sortedbaselist)
