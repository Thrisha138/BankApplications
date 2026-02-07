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
    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")

    account = BankAccount(name, acc_no)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.display_details()

        elif choice == "5":
            print("Thank you for using Bank Application!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
