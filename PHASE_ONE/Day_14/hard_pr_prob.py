# In this we will solve some hard level pr problems

#Q7. Build a complete School system:

#Person → base class
#Student(Person) → marks, grades, attendance
#Teacher(Person) → subjects, salary
#Course → course name, teacher, enrolled students
#School → manages students, teachers, courses
#School.add_student(), enroll_student_in_course()
#School.generate_report() → full school summary

# ---------------- Person Base Class ----------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ---------------- Student Class ----------------

class Student(Person):
    def __init__(self, name, age, marks, grade, attendance):
        super().__init__(name, age)
        self.marks = marks
        self.grade = grade
        self.attendance = attendance


# ---------------- Teacher Class ----------------

class Teacher(Person):
    def __init__(self, name, age, subjects, salary):
        super().__init__(name, age)
        self.subjects = subjects      # list
        self.salary = salary


# ---------------- Course Class ----------------

class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)


# ---------------- School Class ----------------

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
