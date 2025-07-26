nums=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
search_no=int(input("which number you want to search"))
i=0
j=len(nums)
is_present=0
while i<j:
    if(nums[i]==search_no):
        is_present=1
        break
    else:
        i+=1
if(is_present==1):
    print(search_no,"is Present at index",i)
else:
    print(search_no,"is not Present")
