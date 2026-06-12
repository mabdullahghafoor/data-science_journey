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
    def add_marks(self, subject, marks):
        if not 0 <= marks <= 100:
            raise ValueError(f"Invalid marks: {marks}")
        self.__marks[subject] = marks
        print(f"✅ {subject}: {marks} added for {self.name}")

