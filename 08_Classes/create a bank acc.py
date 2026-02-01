#create a account with 2 atributes- balance and account number,

class Account:
    def __init__(self, bal, acc):
        self.balance = bal 
        self.account_number = acc
    #debbit method 
    def debit(self, amount):
        self.balance -= amount
        print("Rs" , amount, "was debited")
        print("total balance=", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs" , amount, "was credited")  
        print("total balance=", self.get_balance())  
    def get_balance (self):
        return self.balance     
acc1 = Account(86000, 39060)
acc1.debit(555)