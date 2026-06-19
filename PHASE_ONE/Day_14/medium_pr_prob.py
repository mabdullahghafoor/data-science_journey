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

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.__balance:
            print("Insufficient Balance!")
        else:
            self.__balance -= amount
            self.transactions.append(f"Withdrew {amount}")


    @property
    def balance(self):
        return self.__balance

    def print_statement(self):
        print("Account Details")
        print(f"Account Holder: {self.owner}")
        print(f"Account Balance: {self.__balance}")
        print(f"\nTransaction History")
        for transaction in self.transactions:
            print(transaction )



# Q5. Create a Person parent class, then
#Student and Teacher child classes.
