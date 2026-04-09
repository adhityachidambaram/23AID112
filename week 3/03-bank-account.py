class BankAccount:
    def __init__(self, id):
        self.id = id
        self.balance = 0
    
    def deposit(self, amount):
        print(f"depositing : {amount}")
        self.balance += amount
        
    def withdraw(self, amount):
        print(f"withdrawing : {amount}")
        self.balance -= amount
        
    def __str__(self):
        return f"id = {self.id}, balance = {self.balance}"
        
acc1 = BankAccount(100)
print(acc1)

acc1.deposit(1000)
print(acc1)

acc1.deposit(2000)
print(acc1)

acc1.withdraw(500)
print(acc1)

acc1.withdraw(1500)
print(acc1)


        