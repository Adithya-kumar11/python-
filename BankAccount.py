class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")
        return self.balance



account = BankAccount("Adithya", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
account.check_balance()