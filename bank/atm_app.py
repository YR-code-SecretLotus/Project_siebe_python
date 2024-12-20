from bank_account import BankAccount


def print_balance(account):
    print(f"Current balance: €{account.balance:.2f}")


def login(accounts):
    attempts = 0
    while attempts < 3:
        account_id = input("Enter your account number: ")
        for account in accounts:
            if account.account_id == account_id:
                pin_code = input("Enter your PIN code: ")
                if pin_code == account.pin_code:
                    print(f"Welcome, {account.holder_name}")
                    return account
                else:
                    print("Incorrect PIN.")
                    attempts += 1
                    break
        if attempts < 3:
            print("Account number not found. Please try again.")
    print("Too many failed attempts. Exiting.")
    exit()


def main():
    # Maak meerdere BankAccount objecten aan
    accounts = [
        BankAccount(account_id="123456", pin_code="1234", holder_name="yoeri de raaf", balance=100),
        BankAccount(account_id="654321", pin_code="5678", holder_name="carl de wijze", balance=500),
        BankAccount(account_id="111222", pin_code="9876", holder_name="mia je weet wel", balance=300)
    ]

    # Gebruiker inloggen
    account = login(accounts)

    # welkom printen
    print("******************************")
    print("******************************")
    print("**     ATM Appclication     **")
    print("******************************")
    print("******************************")
    print("******************************")
    # Print het saldo van de rekening
    print_balance(account)


    # Welkom-menu voor de gebruiker
    while True:
        print("\nChoose an option:")
        print("*1. Deposit      *")
        print("*2. Withdraw     *")
        print("*3. Exit         *")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print_balance(account)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
            print_balance(account)
        elif choice == "3":
            print("*    shutting down...    *")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
