import json


class Student:
    """Complete student entity."""

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def add_marks(self, subject, marks):

        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")

        self.marks[subject] = marks

    @property
    def total(self):
        return sum(self.marks.values())

    @property
    def percentage(self):

        if len(self.marks) == 0:
            return 0

        return self.total / len(self.marks)

    @property
    def grade(self):

        if self.percentage >= 80:
            return "A"

        elif self.percentage >= 70:
            return "B"

        elif self.percentage >= 60:
            return "C"

        elif self.percentage >= 50:
            return "D"

        return "F"

    @property
    def passed(self):
        return self.percentage >= 50

    def print_card(self):

        print("\n-----------------------")
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")

        for subject, marks in self.marks.items():
            print(f"{subject:<10}: {marks}")

        print(f"Total      : {self.total}")
        print(f"Percentage : {self.percentage:.2f}%")
        print(f"Grade      : {self.grade}")

    def __str__(self):
        return (
            f"{self.roll_no} - "
            f"{self.name} ({self.percentage:.2f}% | {self.grade})"
        )