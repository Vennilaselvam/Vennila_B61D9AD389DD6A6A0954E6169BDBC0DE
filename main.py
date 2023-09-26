class BankAccount:

  def __init__(self, account_number, account_holder, initial_balance=0):
    self.__account_number = account_number
    self.__account_holder = account_holder
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
    else:
      print("Invalid deposit amount. Amount must be greater than 0.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
    elif amount <= 0:
      print("Invalid withdrawal amount. Amount must be greater than 0.")
    else:
      print("Insufficient funds for withdrawal.")

  def display_balance(self):
    print(
        f"Account Balance for {self.__account_holder}'s account: ${self.__account_balance}"
    )


# Example usage:
if __name__ == "__main__":
  # Create an instance of BankAccount
  my_account = BankAccount("123456789", "John Doe", 1000)

  # Deposit and display balance
  my_account.deposit(500)
  my_account.display_balance()

  # Withdraw and display balance
  my_account.withdraw(200)
  my_account.display_balance()

  # Attempt to withdraw more than the balance
  my_account.withdraw(1500)
  
