# Exercise 1 from python OOP Udemy course

class Account:
    def set_details(self, name, balance):
        self.balance = balance
        self.name = name

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def display(self) :
        print(self.name, self.balance)

account1 = Account()
account2 = Account()

account1.set_details("Ignacio", 5000)
account1.deposit(1500)
account1.display()
account1.withdraw(1500)
account1.display()