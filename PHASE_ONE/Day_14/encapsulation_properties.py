# In this how to use encapsulte in oops

# ── Encapsulation: protect data from direct modification ──────────
# Private variables use _ or __ prefix

class BankAccount:
    """A bank account with protected balance."""

    def __init__(self, owner, initial_balance):
        self.owner    = owner
        self.__balance = initial_balance    # __ = private!
        self.__transactions = []

