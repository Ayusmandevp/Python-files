str=input("Enter the String:")
idx=int(input("Enter the index no to be removed:"))
newstr=""
for el in range(0,len(str),1):
    if(el==idx):
        continue
    else:
        newstr+=str[el]
print("Your new String is",newstr)