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

    def get_marks(self):
        return dict(self.__marks)   # return copy, not original

    # ── Computed properties ───────────────────────────────────────
    @property
    def total(self):
        return sum(self.__marks.values())

    @property
    def percentage(self):
        if not self.__marks:
            return 0
        return round(self.total / (len(self.__marks) * 100) * 100, 2)

    @property
    def grade(self):
        p = self.percentage
        if   p >= 90: return "A+"
        elif p >= 80: return "A"
        elif p >= 70: return "B"
        elif p >= 60: return "C"
        elif p >= 50: return "D"
        else:         return "F"

    @property
    def status(self):
        all_pass = all(m >= 40 for m in self.__marks.values())
        return "Pass ✅" if all_pass and self.percentage >= 50 \
               else "Fail ❌"

    # ── Display ───────────────────────────────────────────────────
    def print_card(self):
        print(f"\n{'─'*42}")
        print(f"  [{self.student_id}] {self.name}")
        print(f"{'─'*42}")
        for subject, marks in self.__marks.items():
            print(f"  {subject:<15}: {marks}/100")
        print(f"{'─'*42}")
        print(f"  Total      : {self.total}/{len(self.__marks)*100}")
        print(f"  Percentage : {self.percentage}%")
        print(f"  Grade      : {self.grade}")
        print(f"  Status     : {self.status}")

    def __str__(self):
        return f"Student({self.student_id}: {self.name}, {self.percentage}%)"


# ── Using the system ──────────────────────────────────────────────
s1 = Student("STU001", "Ali Hassan",  22)
s2 = Student("STU002", "Sara Ahmed",  21)
s3 = Student("STU003", "Fatima Khan", 23)

subjects = ["Math", "English", "Science", "Urdu", "CS"]
marks_data = {
