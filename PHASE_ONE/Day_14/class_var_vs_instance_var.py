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
