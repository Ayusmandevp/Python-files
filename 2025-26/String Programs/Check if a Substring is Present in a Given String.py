str=input("Enter the String:")
substr=input("Enter the Substring:")
str2=str.lower()
substr2=substr.lower()
if(str2.find(substr2)==-1):
    print(substr,"is not present in",str)
else:
    print(substr,"is present in",str)
print("Note:Uppercase and lowercase has same meaning here")