# # Python program to create Bankaccount class
# # with both a deposit() and a withdraw() function
# class Bank_Account:
#     def __init__(self):
#         self.balance=0
#         print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

#     def deposit(self):
#         amount=float(input("Enter amount to be Deposited: "))
#         self.balance += amount
#         print("\n Amount Deposited:",amount)

#     def withdraw(self):
#         amount = float(input("Enter amount to be Withdrawn: "))
#         if self.balance>=amount:
#             self.balance-=amount
#             print("\n You Withdrew:", amount)
#         else:
#             print("\n Insufficient balance  ")

#     def display(self):
#         print("\n Net Available Balance=",self.balance)

# # Driver code
 
# # creating an object of class
# s = Bank_Account()
 
# # Calling functions with that class object
# s.deposit()
# s.withdraw()
# s.display()
# print("-------------------------------------------------------------")
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute

    # Getter method to access the private balance
    def get_balance(self):
        return self.__balance

    # Setter method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    # Setter method to withdraw money
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

# Example usage
account = BankAccount("Rahul", 5000)
print(f"Account Holder: {account.account_holder}")
print(f"Current Balance: ₹{account.get_balance()}")

account.deposit(2000)
print(f"Updated Balance: ₹{account.get_balance()}")

account.withdraw(3000)
print(f"Final Balance: ₹{account.get_balance()}")
