rotation_value=int(input("Enter rotation value:"))
str_value=input("Enter String:")

while True:
    type_rotation=input("Enter rotation type(left or right):")
    if type_rotation.lower()=="left":
        print(str_value[rotation_value:] + str_value[:rotation_value])
        break
    elif type_rotation.lower()=="right":
        print(str_value[-rotation_value:] + str_value[:-rotation_value])
        print
    else:
        print("choose left or right...")