# In this we see how to make classes and use them

# ── Class definition ─────────────────────────────────────────────
#
#   class ClassName:          ← PascalCase naming convention
#       def __init__(self):   ← constructor (runs at creation)
#           self.attribute    ← instance variable
#
#       def method(self):     ← instance method
#

class Students:

     """Represents a student in the system."""

    # ── Constructor: runs automatically when object is created ───

def __init__ (self, name, age, cgpa):
    # self = the specific object being created
    # self.name = instance variable (belongs to THIS object)
    self.name = name
    self.age = age
    self.cgpa = cgpa
