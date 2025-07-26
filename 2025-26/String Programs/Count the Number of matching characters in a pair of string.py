str=input("Enter the string:")
matched=""
str=str.lower()
for el in range(0,len(str),1):
    if ((matched.find(str[el]))==-1):
        if ((str.count(str[el]))>=2):
            matched+=str[el]
    
print("matched characters are",matched)
print("Total no of matching characters are",len(matched))