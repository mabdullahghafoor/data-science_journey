# In this we will se some difference between class variables and instance variables

class Student:
    # ── Class variable: SHARED by ALL objects ────────────────────
    school_name   = "FAST-NUCES"
    total_students = 0

    def __init__(self, name, marks):
        # ── Instance variables: UNIQUE to each object ────────────
        self.name  = name
        self.marks = marks
        Student.total_students += 1     # increment shared counter

    def get_info(self):
        print(f"[{Student.school_name}] {self.name}: {self.marks}")

# ── Creating students ─────────────────────────────────────────────
s1 = Student("Ali",    [88, 76, 92])
s2 = Student("Sara",   [65, 82, 71])
s3 = Student("Fatima", [95, 98, 100])

s1.get_info()   # [FAST-NUCES] Ali: [88, 76, 92]
s2.get_info()   # [FAST-NUCES] Sara: [65, 82, 71]

# Class variable is shared — all students see same value
print(Student.total_students)   # 3
print(s1.total_students)        # 3 (accessible from object too)
