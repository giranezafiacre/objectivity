class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. Your new balance is {self.balance}.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal unsuccessful. Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawal successful. Your new balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def check_balance(self):
        print(f"Your current balance is {self.balance}.")

# main function to run the program
def main():
    print("Welcome to our bank. Please select an option:")
    print("1. Create new account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Exit")

    accounts = {}

    while True:
        try:
            option = int(input("> "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            name = input("Please enter your name: ")
            if name in accounts:
                print("Account already exists.")
            else:
                accounts[name] = BankAccount(name)
                print(f"Account created successfully for {name}.")

        elif option == 2:
            name = input("Please enter your name: ")
            if name not in accounts:
                print("Account not found.")
            else:
                try:
                    amount = float(input("Please enter deposit amount: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                accounts[name].deposit(amount)

        elif option == 3:
            name = input("Please enter your name: ")
            if name not in accounts:
                print("Account not found.")
            else:
                try:
                    amount = float(input("Please enter withdrawal amount: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                accounts[name].withdraw(amount)

        elif option == 4:
            name = input("Please enter your name: ")
            if name not in accounts:
                print("Account not found.")
            else:
                accounts[name].check_balance()

        elif option == 5:
            print("Thank you for using our bank. Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
