class Car:
    def _init_(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")

car1= Car()
car1.start()   #here only nasesarry detail is shown

