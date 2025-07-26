n=int(input("Enter the number"))
factorial=1
for el in range(n,0,-1):
    factorial*=el

print("factorial is",factorial)