str=input("Enter the string:")
newstr=""
str=str.lower()
for el in range(0,len(str),1):
    if ((newstr.find(str[el]))==-1):
        newstr+=str[el]
print("new string is",newstr)
        