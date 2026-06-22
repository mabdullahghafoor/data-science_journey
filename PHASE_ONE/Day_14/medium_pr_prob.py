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


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def introduce(self):
        print(f"Hello, I am teacher {self.name} and I teach students.")


# Creating objects
s1 = Student("Ali", 20)
t1 = Teacher("Mr. Khalid", 40)

# Method overriding in action
s1.introduce()
t1.introduce()

# isinstance check
print(isinstance(s1, Person))  # True
print(isinstance(t1, Person))  # True


#Q6. Build a Library class that:

#Stores a collection of books (dict)
#add_book(title, author, copies)
#borrow_book(title) → reduces copies
#return_book(title) → increases copies
#search(title) → find book details
#list_available() → only books with copies > 0

class Library:
    def __init__(self):
        # Stores books as:
        # {"Python Basics": {"author": "John Smith", "copies": 3}}
        self.books = {}

    def add_book(self, title, author, copies):
        self.books[title] = {
            "author": author,
            "copies": copies
        }

    def borrow_book(self, title):
        if title not in self.books:
            print("Book not found!")
        elif self.books[title]["copies"] <= 0:
            print("No copies available!")
        else:
            self.books[title]["copies"] -= 1
            print(f"You borrowed '{title}'.")

    def return_book(self, title):
        if title not in self.books:
            print("Book not found!")
        else:
            self.books[title]["copies"] += 1
            print(f"You returned '{title}'.")

    def search(self, title):
        if title in self.books:
            book = self.books[title]
            print("Book Found!")
            print(f"Title : {title}")
            print(f"Author: {book['author']}")
            print(f"Copies: {book['copies']}")
        else:
            print("Book not found!")

    def list_available(self):
        print("\nAvailable Books:")
        for title, details in self.books.items():
            if details["copies"] > 0:
                print(f"{title} by {details['author']} "
                      f"({details['copies']} copies)")


# ---------------- Testing ----------------

library = Library()
