# list=[1,2,3,4,23,4,5,7]
# while(len(list)!=0):
#     list.pop(0)
# print("list:",list)
# print("list is now Empty")

list=[1,2,3,4,5]
def clearlist(list):
    list.pop(0)
    if (len(list)==0):
        return
    else:
        clearlist(list)
clearlist(list)
print("list:",list)
print("list is now Empty")