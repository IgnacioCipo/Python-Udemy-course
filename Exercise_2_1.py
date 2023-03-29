# Exercise 2 from python OOP Udemy course

class Account:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def display(self) :
        print(self.name, self.balance)

account1 = Account("Ignacio", 5000)
account2 = Account("Spunky", 6000)

account1.deposit(1500)
account1.display()
account1.withdraw(1500)
account1.display()