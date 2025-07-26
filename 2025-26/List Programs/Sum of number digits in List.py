list=[123,234,644,123234,23456,2345679]
totalsum=0
for i in list:
    sum=0
    while i>0:
        digit=i%10
        sum+=digit
        i=int(i/10)
    print("Sum of all digits is",sum)
    totalsum+=sum
print("sum of all digits present in list is",totalsum)