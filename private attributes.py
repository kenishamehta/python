class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def __reset_pass(Self):
        print(Self.__acc_pass)

acc1 = Account("12345","abcdef")

print(acc1.acc_no)
# print(acc_pass)
print(acc1.__reset_pass())