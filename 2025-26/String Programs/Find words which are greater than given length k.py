length=int(input("Enter the length:"))
while True:
    str=input("Enter the string:")
    if(len(str)==length):
        print(str,"is a string of same length as given")
    else:
        print(str,"is not a string of same length as given")
    checking=input("Wanna checking more? Enter NO for Sop otherwise press anything...")
    if(checking=='NO'or checking=='No'or checking=='nO'or checking=='no'):
        break
print("Thank you for visiting...")