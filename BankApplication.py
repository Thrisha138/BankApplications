class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def display_details(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.acc_no)
        print("Balance: ₹", self.balance)


def main():
    print("===== Welcome to Bank Application =====")

    # Predefined values for Jenkins (NO input)
    name = "Thrisha"
    acc_no = "ACC12345"

    account = BankAccount(name, acc_no, 5000)

    # Automated operations
    account.display_details()
    account.deposit(2000)
    account.withdraw(1500)
    account.check_balance()

    print("\nBank Application executed successfully!")


if __name__ == "__main__":
    main()
