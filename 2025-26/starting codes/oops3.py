class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    #debit
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"has been debited")
        print("Total balance is",self.balance)

    #credit
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"has been credited")
        print("Total balance is",self.balance)

    #print
    def print_balance(self):
        print("Total balance is",self.balance)



acc1=Account(100000,123456789)
acc1.debit(5000)
acc1.credit(1000000)
acc1.print_balance()

