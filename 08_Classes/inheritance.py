#when one class derives the properties of other class than it is called inheritance it is of three types-1 single 2)multi level 3)multiple inheritance.
class Car:
    def start():
        print("car started..")
    def stop():
        print("car stopped") 

class toyotacar(Car):
    def __init__(self, name):
        self.name = name

car1 = toyotacar("fortuner")
print (car1.name)