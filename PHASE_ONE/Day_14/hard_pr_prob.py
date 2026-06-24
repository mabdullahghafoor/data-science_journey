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
