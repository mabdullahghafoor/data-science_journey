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

    def subject_average(self, subject):

        marks = []

        for student in self.students:

            if subject in student.marks:
                marks.append(student.marks[subject])

        if not marks:
            return 0

        return sum(marks) / len(marks)

    def generate_report(self):

        print("\n========== CLASS REPORT ==========")

        print(f"Class Name: {self.name}")
        print(f"Students  : {len(self.students)}")

        print(
            f"Class Average: "
            f"{self.class_average():.2f}%"
        )

        topper = self.get_topper()

        if topper:
            print(
                f"Topper: {topper.name} "
                f"({topper.percentage:.2f}%)"
            )

        print("\nStudents:")

        for student in self.students:
            print(student)

    def save_to_file(self, filename):

        data = []

        for student in self.students:

            data.append({
                "roll_no": student.roll_no,
                "name": student.name,
                "marks": student.marks
            })

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename):

        try:

            with open(filename, "r") as file:
                data = json.load(file)

            self.students.clear()

            for record in data:

                student = Student(
                    record["roll_no"],
                    record["name"]
                )

                student.marks = record["marks"]
