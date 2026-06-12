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

    def introduce(self):
        print(f"Hi! I'm {self.name}, {self.age} years old.")

    def get_info(self):
        return f"{self.name} | {self.email}"

# ── CHILD class: inherits from Person ────────────────────────────
class Student(Person):
    """Student inherits from Person."""

    def __init__(self, name, age, email, student_id, marks):
        super().__init__(name, age, email)  # call parent __init__!
        self.student_id = student_id        # student-specific
        self.marks      = marks

    def get_percentage(self):
        return (sum(self.marks) / (len(self.marks) * 100)) * 100

    # Override parent method → customize for Student
