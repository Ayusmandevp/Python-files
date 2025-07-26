str=input("Enter the String:")
strnew=str.lower()
for el in range(0,len(strnew)-1,1):
    if(strnew[el]!=strnew[(len(strnew)-1)-el]):
        print(str,"is not a Palindrome.(Uppercase and Lower case has not taken into consideration and spaces matter...)")
        break
else:
    print(str,"is a Palindrome.(Uppercase and Lower case has not taken into consideration and spaces matter...)")
