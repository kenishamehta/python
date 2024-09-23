 #Inheritance
#single
class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Hondacity(Car):
    def __init__(self,name):
        self.name=name

car1=Hondacity("model1")
car2=Hondacity("model2")
print(car1.name)