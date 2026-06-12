# In this how to use encapsulte in oops

# ── Encapsulation: protect data from direct modification ──────────
# Private variables use _ or __ prefix

class BankAccount:
    """A bank account with protected balance."""

    def __init__(self, owner, initial_balance):
        self.owner    = owner
        self.__balance = initial_balance    # __ = private!
        self.__transactions = []

    # ── Property: access private data safely ─────────────────────
    @property
    def balance(self):
        """Read-only access to balance."""
        return self.__balance

    # ── Methods to modify private data ───────────────────────────
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self.__balance += amount
        self.__transactions.append(f"+{amount}")
        print(f"✅ Deposited PKR {amount:,}. Balance: {self.__balance:,}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        if amount > self.__balance:
            raise ValueError("Insufficient balance!")
        self.__balance -= amount
        self.__transactions.append(f"-{amount}")
        print(f"✅ Withdrawn PKR {amount:,}. Balance: {self.__balance:,}")

    def get_statement(self):
        print(f"\n📋 Account: {self.owner}")
        print(f"   Transactions: {self.__transactions}")
        print(f"   Balance: PKR {self.__balance:,}")

# ── Using the class ───────────────────────────────────────────────
account = BankAccount("Ali Hassan", 50000)

print(account.balance)      # 50000 ✅ via property
