# ═══════════════════════════════════════════════════
# FILE    : models/student.py
# PURPOSE : Student class — core data model
# USES    : OOP, Properties, Exception Handling
# ═══════════════════════════════════════════════════

class Student:
    """
    Represents a student in the PyVault system.
    Demonstrates: OOP, Encapsulation, Properties
    """

    # Class variable — shared across all students
    SUBJECTS      = ["Math", "English", "Science", "Urdu", "CS"]
    PASSING_MARK  = 40
    PASSING_PCT   = 50
    total_count   = 0

    def __init__(self, student_id, name, age, city, email):
        # Instance variables
        self.student_id = student_id
        self.name       = name
        self.age        = age
        self.city       = city
        self.email      = email
        self.__marks    = {}        # private — encapsulation!
        Student.total_count += 1

    # ── Marks Management ─────────────────────────────────────────
    def add_marks(self, subject, marks):
        """Add marks for a subject with validation."""
        if subject not in self.SUBJECTS:
            raise ValueError(f"Invalid subject: {subject}")
        if not isinstance(marks, (int, float)):
            raise TypeError("Marks must be a number!")
        if not 0 <= marks <= 100:
            raise ValueError(f"Marks must be 0-100, got {marks}")
        self.__marks[subject] = marks

    def get_marks(self):
        """Return copy of marks dict — encapsulation."""
        return dict(self.__marks)

    def has_marks(self):
        """Check if student has any marks entered."""
        return len(self.__marks) > 0

    # ── Computed Properties ───────────────────────────────────────
    @property
    def total(self):
        return sum(self.__marks.values()) if self.__marks else 0

    @property
    def percentage(self):
        if not self.__marks:
            return 0.0
        return round(
            (self.total / (len(self.__marks) * 100)) * 100, 2
        )

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
        if not self.__marks:
            return "Pending ⏳"
        all_pass = all(
            m >= self.PASSING_MARK
            for m in self.__marks.values()
        )
        return ("Pass ✅"
                if all_pass and self.percentage >= self.PASSING_PCT
                else "Fail ❌")

    # ── Serialization (for file saving) ──────────────────────────
    def to_dict(self):
        """Convert student to dictionary for JSON saving."""
        return {
            "student_id": self.student_id,
            "name"      : self.name,
            "age"       : self.age,
            "city"      : self.city,
            "email"     : self.email,
            "marks"     : self.__marks,
        }

    @classmethod
    def from_dict(cls, data):
        """Create Student object from dictionary (JSON loading)."""
        s = cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["city"],
            data["email"]
        )
        for subject, marks in data.get("marks", {}).items():
            s.add_marks(subject, marks)
        return s

    # ── Display ───────────────────────────────────────────────────
    def print_card(self):
        """Print formatted student report card."""
        print(f"\n  ╔{'═'*44}╗")
        print(f"  ║  📋 REPORT CARD{' '*28}║")
        print(f"  ╠{'═'*44}╣")
        print(f"  ║  ID     : {self.student_id:<33}║")
        print(f"  ║  Name   : {self.name:<33}║")
        print(f"  ║  Age    : {self.age:<33}║")
        print(f"  ║  City   : {self.city:<33}║")
        print(f"  ╠{'═'*44}╣")

        if self.__marks:
            print(f"  ║  {'SUBJECT':<15} {'MARKS':>6} {'STATUS':>10}{'':>11}║")
            print(f"  ║  {'─'*42}  ║")
            for subject, marks in self.__marks.items():
                st = "✅" if marks >= self.PASSING_MARK else "❌"
                print(f"  ║  {subject:<15} {marks:>6}/100 "
                      f"{st:>10}{'':>11}║")
            print(f"  ╠{'═'*44}╣")
            print(f"  ║  Total      : "
                  f"{self.total}/{len(self.__marks)*100}"
                  f"{'':>26}║")
            print(f"  ║  Percentage : {self.percentage}%"
                  f"{'':>29}║")
            print(f"  ║  Grade      : {self.grade:<33}║")
            print(f"  ║  Status     : {self.status:<33}║")
        else:
            print(f"  ║  No marks entered yet.{'':>21}║")

        print(f"  ╚{'═'*44}╝")

    def __str__(self):
        return (f"[{self.student_id}] {self.name} "
                f"| {self.percentage}% | {self.grade}")

    def __lt__(self, other):
        return self.percentage < other.percentage

    def __gt__(self, other):
        return self.percentage > other.percentage