# A class method is bound to the class and receive the class as an implicit first argument.

class Person:
    name = "anonymous"
    @classmethod
    def changeName (cls, name):
        cls.name = name 
p1 = Person()
p1.changeName("rashpal") 
print(p1.name) 
print(Person.name)      