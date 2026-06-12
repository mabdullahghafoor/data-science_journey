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



# ── Method: function that belongs to this class ───────────────
def introduce(self):
    print(f"Hi! I'm {self.name}, age {self.age}.")

def get_status(self):
    status = "Dean's List 🌟" if self.cgpa >= 3.7 else "Regular"
    return status


# ── Creating Objects (Instances) ─────────────────────────────────
student1 = Students("Ali Hassan",  22, 3.87)  # object 1
student2 = Students("Sara Ahmed",  21, 3.52)  # object 2
student3 = Students("Fatima Khan", 23, 3.95)  # object 3


# ── Using object attributes ───────────────────────────────────────
print(student1.name)        # Ali Hassan
print(student2.age)         # 21
print(student3.cgpa)        # 3.95
