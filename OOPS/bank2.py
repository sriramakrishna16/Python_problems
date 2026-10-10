import random

class Account:
    def __init__(self, name, balance):
        number = random.randint(0, 999999)

        self.accountNo = number
        self.name = name
        self.balance = balance


class Customer(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdraw of {amount} failed due to : Insufficient balance")
        elif amount <= 0:
            print("Withdraw failed")
        else:
            self.balance -= amount
            print("withdraw successfull , remaining balance is ", self.balance)

    def deposit(self, amount):
        if amount < 0:
            print("amount cannot be negative")
        else:
            self.balance += amount
            print(f"Deposit amount of {amount} successful and the remaining balance is {self.balance}")

    def printDetails(self):
        print("Name : ", self.name)
        print("Account no : ", self.accountNo)
        print("Balance : ", self.balance)

class Bank:

    # @staticmethod
    def main():
        c1 = Customer("ram", 500)
        c1.withdraw(5000)
        c1.deposit(1000)
        c1.printDetails()
        

if __name__ == "__main__":
    Bank.main()


