import json


class Student:
    """Complete student entity."""

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def add_marks(self, subject, marks):

        if not (0 <= marks <= 100):
