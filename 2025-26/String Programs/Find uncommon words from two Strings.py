def finduncommon(str1,str2):
    uncommon=set()
    for el in range(0,len(str1),1):
        if (str2.find(str1[el])==-1):
            uncommon.add(str1[el])
    return uncommon
str1=input("enter string one:")
str2=input("enter string two:")
str1lower=str1.lower()
str2lower=str2.lower()
print(finduncommon(str1lower,str2lower))
print(finduncommon(str2lower,str1lower))
print("Uncommon words are",(finduncommon(str1lower,str2lower)).union(finduncommon(str2lower,str1lower)))