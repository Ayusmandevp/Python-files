n=int(input("Enter the number till which you want to print all prime numbers till them:"))
i=2
while i<=n:
    j=2
    while j<i:
        if(i%j==0):
            break
        j+=1
    else:
        print(i)
    i+=1
            

print("Program execution completed")
