str=input("Enter the String:")
repeat=""
lower_str=str.lower()
for el in range(0,len(lower_str),1):
    if(repeat.find(lower_str[el])!=-1):
        continue
    else:
        if(lower_str[el]==" "):
            print("The frequency of blank space ' ' in",str,"is",lower_str.count(lower_str[el]))
        else:
            print("The frequency of" ,lower_str[el],"in",str,"is",lower_str.count(lower_str[el]))
        repeat+=lower_str[el]
print("Note:Uppercase and lowercase has same meaning here")