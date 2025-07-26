list=[1,2,9,(),2,3,(),()]
new=[]
for i in list:
    if i:
        new.append(i)
print(new)

# for i in list:
#     if i==():
#         list.remove(i)         # list length change might ignore some element while getting renewed
# print(list)