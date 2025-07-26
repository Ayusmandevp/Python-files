# n=int(input("Enter the number till which you want to print sum of squares:"))
# sum=0
# for num in range(1,n+1,1):
#     sum+=num*num
# print("sum of squares of first",n,"numbers is:",sum)

# print("The answer through shortcut formula is:",(n*(n+1)*(2*n+1)/6))





#USING RECURSION

n=int(input("Enter the number till which you want to print sum of squares:"))
def squareofnum(n):
    if (n==1):
        return 1
    else:
        return n*n+squareofnum(n-1)
sum=squareofnum(n)
print("sum of squares of first",n,"numbers is:",sum)
print("The answer through shortcut formula is:",(n*(n+1)*(2*n+1)/6))