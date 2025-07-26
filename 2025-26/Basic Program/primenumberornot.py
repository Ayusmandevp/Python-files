n=int(input("Enter the number till which you want to print all prime numbers till them:"))
isprime=1
i=2
while i<n:
    if n%i==0:
        print(n,"is not a prime number")
        break
    else:
        i+=1
else:
    print(n,"is a prime number")

