#  Encapsulation - Protecting Attributes: Implement a class Account with a private attribute balance and provide methods to deposit and withdraw safely, checking for sufficient funds.


class Account:
    def __init__(self,balance=0):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient amount...try again...")
    def check_balance(self):
        print(f"Remaining balance: {self.__balance}")


acc1=Account(200)
acc1.check_balance()
acc1.deposit(500)
acc1.check_balance()
acc1.withdraw(400)
acc1.check_balance()