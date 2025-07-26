str=input("Enter a string in snake case:")
newstr=""
str=str.capitalize()
for el in range(0,len(str),1):
    if(str[el]=="_"):
        newstr+=(str[(el+1):(el+2)]).capitalize()
    elif(str[el-1]=="_"):
        continue
    else:
        newstr+=str[el]
print("Your string in Pascal case is",newstr) 