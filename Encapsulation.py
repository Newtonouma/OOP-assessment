class BankAccount:
    def __init__(self, initial_balance=0):
        # Private balance attribute
        self.__balance = initial_balance

    # Cash Depositing Function
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited KSh. {amount}. New balance is KSh. {self.__balance}.")
        else:
            print("Deposit amount must be a valid amount.")

    # Cash Withdrawal Function
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew KSh. {amount}. New balance is KSh. {self.__balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be a valid amount.")

    # current balance function
    def get_balance(self):
        return self.__balance

# an instance of initial balance of Khs.1000
account = BankAccount(1000)

# Deposit money
account.deposit(200)

# Withdraw money
account.withdraw(150)

# current balance
print(f"Current balance is: KSh.{account.get_balance()}")
