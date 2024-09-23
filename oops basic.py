# class Student:
#     def __init__(self):
#         print("adding new student")
    
#     def __init__(self,fullname):
#         self.name=fullname
#         print("adding new student")

# s1=Student("anjali")
# print(s1.name)

# s2=Student("karan")
# print(s2.name)


class Student:
    clgname="ABC"
     
    @staticmethod
    def hello():
     print("hello")
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def welcome(self):
        print("welcome",self.name)

s1=Student("karan",89)  
s1.welcome() 