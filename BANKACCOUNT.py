"""
BANK ACCOUNT
Davide La Magna
"""

#Declare a class BankAccount
class BankAccount:
#Define methods

    #method init for initializing data
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    #metod str for printing data
    def __str__(self):
        return f"Account information\n Name: {self.name}\n Surname: {self.surname}\n Balance: {self.balance}\n"

    # method read for reading data
    def read(self):
        name = input("Name: ")
        self.name = name
        surname = input("Surname: ")
        self.surname = surname
        balance = input("Balance: ")
        self.balance = balance
        print(BankAccount.__str__(self))


    #methods add and withdraw for adding and withdrawing data
    def add(self):
        add = input("Money to add: ")
        self.balance= int(self.balance)
        self.balance+= int(add)
        print(BankAccount.__str__(self))

    def withdraw(self):
        withdraw = input("Money to withdraw: ")
        if int(withdraw) > int(self.balance):
            print("IMPOSSIBLE.")
        else:
            self.balance -= int(withdraw)
            print(BankAccount.__str__(self))


#example

FirstAcc = BankAccount(" ", " ", " ")
FirstAcc.read()


add = input("Do you want to add money? ")
if add == 'y':
    FirstAcc.add()

withdraw = input("Do you want to withdraw money? ")
if withdraw == 'y':
    FirstAcc.withdraw()

print(FirstAcc.__str__())
