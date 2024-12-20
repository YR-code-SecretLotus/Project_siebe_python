class BankAccount:
    def __init__(self, account_id, pin_code, holder_name, balance=0):
        self.account_id = account_id
        self.pin_code = pin_code
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Amount must be positive.")
