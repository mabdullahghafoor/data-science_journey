import json
from student import Student


class Classroom:

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):

        if not isinstance(student, Student):
            raise TypeError("Must provide Student object")

        self.students.append(student)

    def get_topper(self):

        if not self.students:
            return None

        return max(self.students, key=lambda s: s.percentage)

    def get_failures(self):

        return [student for student in self.students
                if not student.passed]

    def class_average(self):

        if not self.students:
            return 0

        return sum(
            student.percentage
            for student in self.students
        ) / len(self.students)
