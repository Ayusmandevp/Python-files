n=int(input("Enter the number till which you want to print sum of squares:"))
sum=0
for num in range(1,n+1,1):
    sum+=num**3
print("sum of squares of first",n,"numbers is:",sum)

print("The answer through shortcut formula is:",(n*(n+1)/2)**2)





#USING RECURSION

# n=int(input("Enter the number till which you want to print sum of squares:"))
# def cubeofnum(n):
#     if (n==1):
#         return 1
#     else:
#         return n**3+cubeofnum(n-1)
# sum=cubeofnum(n)
# print("sum of squares of first",n,"numbers is:",sum)
# print("The answer through shortcut formula is:",(n*(n+1)/2)**2)