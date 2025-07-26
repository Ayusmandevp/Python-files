str=input("Enter the String")
str=str.lower()
if((str.find("a")>=1)and(str.find("e")>=1)and(str.find("i")>=1)and(str.find("o")>=1)and(str.find("u")>=1)):
    print("all vowels present")
else:
    print("all vowels don't present")