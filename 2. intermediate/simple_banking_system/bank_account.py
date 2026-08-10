class BankAccount:
    def __init__(self, user_name="", balance=0):
        self.user_name = user_name
        self.balance = balance

    def ask_name(self):
        while True:
            name = input("Please enter your name: ").strip()
            if name:
                self.user_name = name
                break
            print("Name cannot be empty.")

    def show_menu(self):
        print("\nMenu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def check_balance(self):
        print(f"Hello {self.user_name}, your balance is ${self.balance}")

    def get_amount(self, action):
        while True:
            try:
                amount = int(input(f"How much would you like to {action}: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

    def deposit(self):
        amount = self.get_amount("deposit")
        self.balance += amount
        print(f"Deposit successful. Current balance: ${self.balance}")

    def withdraw(self):
        amount = self.get_amount("withdraw")
        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        print(f"Withdrawal successful. Current balance: ${self.balance}")

    def main(self):
        self.ask_name()
        print(f"\nHello {self.user_name}!")

        while True:
            self.show_menu()

            try:
                choice = int(input("\nWhat would you like to choose? "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                print("Thank you for using our service.")
                break
            else:
                print("Please enter a number between 1 and 4.")
