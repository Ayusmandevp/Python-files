str=input("Enter the string:")
for el in range(0,len(str),1):
    if(str[el]!="0" and str[el]!="1"):
        print(str,"is not a binary string")
        break
else:
    print(str,"is a binary string")