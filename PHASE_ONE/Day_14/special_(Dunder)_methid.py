# In this we will see how to use Dunderr(Duble UnderScore) Methods

# ── Dunder = Double UNDERscore → __method__ ──────────────────────
# These give your class built-in Python behavior

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks
        self.percentage = (sum(marks) / (len(marks) * 100)) * 100
