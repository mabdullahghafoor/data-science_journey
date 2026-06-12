# In this we will see how canwe use inheritance

# ── Inheritance: child class gets ALL parent features ─────────────
# + can add its own features
# + can override parent methods

# ── PARENT class ─────────────────────────────────────────────────
class Person:
    """Base class for all people."""

    def __init__(self, name, age, email):
        self.name  = name
        self.age   = age
        self.email = email
