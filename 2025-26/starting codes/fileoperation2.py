count=0
with open("number.txt","r") as f:
    data=f.read()
    print(data)


#without split function

# num=""
# for i in range(len(data)):
#     if(data[i]==","):
#         print(int(num))
#         num=""
#     else:
#         num+=data[i]


#with split function

nums=data.split(",")
print(nums)

for val in nums:
    if(int(val)%2==0):
        count+=1

print(count)