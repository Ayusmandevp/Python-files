import string
specialchar=string.punctuation
str=input("Enter the string:")
print("special characters are",specialchar)
present=set()
for el in range(0,len(str),1):
    if(specialchar.find(str[el])!=-1):
        present.add(str[el])
print("All the present special characters are",present)