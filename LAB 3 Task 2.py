class BankAccount:
    def __init__(self, name, acc_num, current_balance):
        """
        Constructor to initialize account details.
        """
        self.current_balance = current_balance
        self.name = name
        self.acc_num = acc_num

    def deposit(self, amount):
        """
        Deposit funds into the account.
        """
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """
        Withdraw funds from the account.
        """
        if amount > 0 and amount <= self.current_balance:
            self.current_balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_holder_info(self):
        """
        Display account holder information.
        """
        print(f"Account holder name: {self.name}")
        print(f"Account number: {self.acc_num}")
        print(f"Current balance: {self.current_balance}")

# Main program
if __name__ == "__main__":
    # Creating an account object
    account = BankAccount("Sabahat", "PKUNI1234557986", 10000)

    # Displaying account information
    account.display_holder_info()
    print()

    # Performing deposit and withdrawal
    account.deposit(10000)
    print()

    account.withdraw(3000)
    account.display_holder_info()
