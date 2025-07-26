list=[1,2,3,4,5,6,7,8]
is_remove='Y'
print("Your list is",list)
while is_remove=='Y' or is_remove=='y':
    is_remove=input("If you want to remove one element press y or Y or if not press n or N")
    if(is_remove=="Y" or is_remove=='y'):
        element=int(input("Enter the element:"))
        for i in list:
            if i==element:
                list.remove(i)
        print("Your updated list is",list)
print("Your final list is",list)
        