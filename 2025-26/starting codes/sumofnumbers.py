# i=1
# sum=0
# n=int(input("Enter the number till which you want to add:"))
# while i<=n:
#     sum+=i
#     i+=1
# print("sum is",sum)
sum=0
n=int(input("Enter the number till you want to add"))
for el in range(1,n+1):
    sum+=el

print("sum is",sum)