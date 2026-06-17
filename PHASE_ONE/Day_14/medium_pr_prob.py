# In This we will solve some medium level problems

#Q4. Build a BankAccount class with:

#Private __balance
#deposit(amount), withdraw(amount)
#@property for balance (read-only)
#Transaction history list
#print_statement() method
#Proper error handling

class BankAccount:

    def __init__(self,owner, initial_balance = 0):
        self.owner = owner
        self.__balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount < 0:
            print(f"Invalid Amount! Amount must be greater than 0")
        else:
            self.__balance += amount
            self.transactions.append(f"Deposited {amount}")
