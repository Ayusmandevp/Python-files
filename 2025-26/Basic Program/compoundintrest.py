p=float(input("Enter Principle(base amount):"))
n=float(input("Enter number of times intrest is compounded per year:"))
r=float(input("Enter rate of intrest in percentage(%) per annum:"))
t=float(input("Enter time in years:"))
a=p*(1+r/n)**n**t
print("Final amount is",a)