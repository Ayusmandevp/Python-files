str=input("Enter the string:")
str=str.lower()
newstr=""
i=1
while (i<len(str)):
    for el in range(0,len(str),1):
        if (newstr.find(str[el])==-1):
            if(str.count(str[el])==i):
                print(str[el])
                newstr+=str[el]
    if(len(newstr)>0):
        break
    i+=1