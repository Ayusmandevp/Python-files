# string=input("Enter a string")
# a=set(i for i in string if string.count(i)>1 and i!=" ")
# print(a)




from collections import Counter

string = input("Enter a string: ")

# Count all characters
char_count = Counter(string)

# Get characters that appear more than once
duplicates = {char for char, count in char_count.items() if count > 1 and char != " "}

print(duplicates)
