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
#Each must have its own introduce() method.
#Show that isinstance(student, Person) is True.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}, and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def introduce(self):
        print(f"Hi, I am student {self.name} and I study at university.")


        print(f"Hello {self.name}, This is Student's class ")

class Teacher(Person):

    def __init__(self):
        pass

    def introduce(self,name):
        self.name = name
        print(f"Hello {self.name}, This is Teacher's class ")


s1 = Student()
t1 = Teacher()

s1.introduce("Ali")
t1.introduce("Sir Khalid")

print(isinstance(s1, Person))