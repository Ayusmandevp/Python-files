str=input("Enter a string:")
newstr=""
restr=input("Wanna replace multiple words with...")
for el in range(0,len(str),1):
    if(newstr.find(str[el])==-1):
        newstr+=str[el]
    else:
        newstr+=restr
print("Your updated string is",newstr)
print("uppercase and lowercase treated differently...")