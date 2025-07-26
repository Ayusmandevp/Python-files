# list=[]
# add="y"
# while(add=='y'or add=="Y"):
#     list.append(input("Enter the element for a list"))
#     add=str(input("Do you want to add more? 'Y' or 'y' for YES and 'N' or 'n'for no:"))
#     if(add=='n' or add=="N"):
#         break

# print("Your list is:",list)

#built in function
# print("Through len() function length of list is",len(list))

# Recursion

list=[1,2,3,4,23,4,5,7]
def count_length(list,count=0):
    if not list:
        return count
    else:
        return 1+count_length(list[1:],count)

length=count_length(list)
print("Through Recursion length of list is",length)