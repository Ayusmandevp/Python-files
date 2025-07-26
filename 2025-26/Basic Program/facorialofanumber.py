num=int(input("Enter the number:"))
factorial=1
for el in range(num,0,-1):
    factorial*=el
print("Factorial of",num,"is",factorial)
