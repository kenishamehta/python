class Employee():
    def __init__(self,role,dept,salary):
        self.role=role
        self.salary=salary
        self.dept=dept

    def showDetails(self):
        print("role= ",self.role)
        print("salary= ",self.salary)
        print("dept= ",self.dept)
        print("name=", self.name)
        print("age= ",self.age)


class Engineeer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","it","40000")

engg1=Engineeer("rahul",40)
engg1.showDetails()