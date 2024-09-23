class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    # def calcPercentage(self):
    #     self.percentage=str((self.phy+sel.chem+self.math)/3)+ "%"
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+ "%"

stud1=Student(98,78,99)
print(stud1.percentage)

stud1.phy=89
print(stud1.percentage)