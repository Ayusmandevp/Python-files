def frequency_method(str):
    total=0
    lower_str=str.lower()
    for el in str:
        total+=1
    print("Length of",str,"is",total)
def lengthmethod(str):
    print("Length of",str,"is",len(str))
def countmethod(str):
    total=str.count("")-1
    print("Length of",str,"is",total)
def enamurateway(str):
    total=0
    for i, str in enumerate(str):
        total+=1
    print("Length is",total)
str=input("Enter the String:")
frequency_method(str)
lengthmethod(str)
countmethod(str)
enamurateway(str)