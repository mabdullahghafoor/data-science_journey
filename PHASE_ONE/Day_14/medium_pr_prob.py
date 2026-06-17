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
