str=input("Enter the String:")
newstr=""
for i in range(len(str)-1,-1,-1):
    newstr+=str[i]
print("new string is",newstr)