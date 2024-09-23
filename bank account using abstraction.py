class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance -= amount
        print("RS.", amount, "was debited")
        print("total balance=",self.get_balance())

    def credit(Self, amount):
        Self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance=",Self.get_balance())

    def get_balance(self):
        return self.balance


acc1= Account(1000000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.debit(2000)
acc1.credit(200)
acc1.credit(10000)