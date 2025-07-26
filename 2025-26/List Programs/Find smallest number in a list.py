# list=[4,5,6,7,2,-5,-123456]
# idx=0
# while(idx<len(list)-1):
#     a=list[idx]
#     b=list[idx+1]
#     if a<=b:
#         smallest=a
#     else:
#         smallest=b
#     idx+=1
#     a=smallest
# print("smallest number is",smallest)




list=[4,5,6,7,2,-5,-123456,8]
idx=0
smallest=list[idx]
while(idx<len(list)-1):
    if smallest>list[idx+1]:
        smallest=list[idx+1]
    idx+=1
print("smallest number is",smallest)
print(list)