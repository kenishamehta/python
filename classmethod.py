class Person:
    name="rahul"
    print(name)

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("kumar")
print(p1.name)
print(Person.name)