class Bank:
    next_an = 10001

    def __init__(self, name, initial_balance = 0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.account_number = Bank.next_an
        Bank.next_an += 1

        self.name = name
        self._balance = initial_balance

        print("account craeted successfully !")
        print("account number : ", self.account_number)


    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        print(f"Deposited : {amount:.2f} by {self.name}")
        print(f"Current Balance: ₹{self._balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount
        print(f"Withdrawn: ₹{amount:.2f}")
        print(f"Current Balance: ₹{self._balance:.2f}")

    def display_details(self):
        print("\n----- Account Details -----")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print(f"Balance: ₹{self._balance:.2f}")
        print("---------------------------")

try:
    account1 = Bank("Rahul", 5000)
    account2 = Bank("Priya", 2000)

    # Operations on Rahul's account
    account1.deposit(1500)
    account1.withdraw(2000)
    account1.display_details()

    # Operations on Priya's account
    account2.deposit(500)
    account2.display_details()

except ValueError as e:
    print("Transaction failed:", e)