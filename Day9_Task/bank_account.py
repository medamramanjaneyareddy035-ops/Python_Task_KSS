# Bank Account System (Class, Object, Constructor) 
'''A bank wants to manage customer accounts. Create a BankAccount class with a 
constructor to initialize account number and balance. Implement methods to deposit, 
withdraw, and display balance.
'''
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def depsoit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)

        else:
            print("Insuffient Balance")

    def display(self):
        print("Account number:", self.account_number)
        print("Balance:", self.balance)

b =  BankAccount(630384, 6000)
b.depsoit(2000)
b.withdraw(1000)
b.display()
