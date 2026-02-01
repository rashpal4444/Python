# Hiding the implimentation detail of a class and only showing the essential feature of the user.


class Car:
    def __init__(self):
       self.acc = False
       self.brk = False
       self.clch = False


    def start (self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()