# list=[4,5,6,7,2,-5,-123456,678]
# idx=0
# while(idx<len(list)-1):
#     a=list[idx]
#     b=list[idx+1]
#     if a>=b:
#         largest=a
#     else:
#         largest=b
#     idx+=1
#     a=largest
# print("largest number is",largest)
# print(list)




list=[4,5,6,7,2,-5,-123456,53]
idx=0
largest=list[idx]
while(idx<len(list)-1):
    if largest<list[idx+1]:
        largest=list[idx+1]
    idx+=1
print("largest number is",largest)
print(list)