class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount}. New Balance: Rs.{self.balance}")
        else:
            print("Invalid deposit amount!")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. Remaining Balance: Rs.{self.balance}")
        else:
            print("Invalid withdraw amount!")

account = BankAccount("Ali Haider" , 10000)
print(f"Account Owner: {account.owner}")
print(f"Initial Balance: {account.balance}")
print()
account.deposit(500)
account.withdraw(1000)
