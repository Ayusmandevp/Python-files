string=input("Enter a recurssive string:")
sub_string=input("Enter a pattern to check:")
length=len(sub_string)
while True:
    a=string.find(sub_string)
    if a==-1:
        if len(string)==0:
            print("possible")
        else:
            print("not possible")
        break
    else:
        string = string[:a] + string[a+length:]