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

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student_in_course(self, student, course):
        course.enroll_student(student)

    def generate_report(self):

        print("\n========== SCHOOL REPORT ==========")

        print("\nStudents:")
        for student in self.students:
            print(
                f"{student.name} | Grade: {student.grade} "
                f"| Marks: {student.marks} "
                f"| Attendance: {student.attendance}%"
            )

        print("\nTeachers:")
        for teacher in self.teachers:
            print(
                f"{teacher.name} | Subjects: {teacher.subjects} "
                f"| Salary: {teacher.salary}"
            )

        print("\nCourses:")
        for course in self.courses:

            print(f"\nCourse: {course.course_name}")
            print(f"Teacher: {course.teacher.name}")

            print("Enrolled Students:")

            for student in course.students:
                print(f"- {student.name}")

        print("\n==================================")


# ---------------- Testing ----------------

# Create school
school = School("ABC School")

# Create students
s1 = Student("Ali", 18, 88, "A", 95)
s2 = Student("Sara", 17, 92, "A+", 98)

# Create teacher
t1 = Teacher("Mr. Khalid", 40, ["Python", "OOP"], 80000)

# Create course
python_course = Course("Python Programming", t1)

# Add data to school
school.add_student(s1)
school.add_student(s2)
