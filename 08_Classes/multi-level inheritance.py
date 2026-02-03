class Car:
    def start(self):
        print("car started..")
    def stop(self):
        print("car stopped..")
class toyotacar(Car):
    def __init__(self,  brand):
        self.brand = brand   
class fortuner(toyotacar):
    def __init__(self, type):
        self.type = type
car1 = toyotacar('fortuner') 

print(car1.start() )

