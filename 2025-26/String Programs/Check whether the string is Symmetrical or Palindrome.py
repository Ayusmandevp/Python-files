def isPalindrome(str):
    strnew=str.lower()
    for el in range(0,len(strnew)-1,1):
        if(strnew[el]!=strnew[(len(strnew)-1)-el]):
            print(str,"is not a Palindrome.(Uppercase and Lower case has not taken into consideration and spaces matter...)")
            break
    else:
        print(str,"is a Palindrome.(Uppercase and Lower case has not taken into consideration and spaces matter...)")
def isSymmetrical(str):
    strnew=str.lower()
    if (len(strnew)%2!=0):
        print(str,"is not a Symmetric.(Uppercase and Lower case has not taken into consideration and spaces matter...)")
    else:
        tillidx=int (len(strnew)/2 )           #before this index all will be one str and from this all will be another
        str1=strnew[0:tillidx]
        str2=strnew[tillidx:len(strnew)]
        if(str1==str2):
            print(str,"is a Symmetric.(Uppercase and Lower case has not taken into consideration and spaces matter...)")
        else:
            print(str,"is not a Symmetric.(Uppercase and Lower case has not taken into consideration and spaces matter...)")

#Main function
str=input("Enter the String:")
isPalindrome(str)
isSymmetrical(str)