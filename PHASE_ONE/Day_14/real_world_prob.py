# In this we will see a real world problem

# ── A mini Student Management System using OOP ───────────────────

class Student:
    """Complete student with all functionality."""

    total_students = 0

    def __init__(self, student_id, name, age):
        self.student_id  = student_id
        self.name        = name
        self.age         = age
        self.__marks     = {}       # private: subject → marks
        Student.total_students += 1

    # ── Marks management ─────────────────────────────────────────
