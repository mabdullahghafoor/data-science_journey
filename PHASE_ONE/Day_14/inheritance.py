# In this we will see how canwe use inheritance

# ── Inheritance: child class gets ALL parent features ─────────────
# + can add its own features
# + can override parent methods

# ── PARENT class ─────────────────────────────────────────────────
class Person:
    """Base class for all people."""

    def __init__(self, name, age, email):
        self.name  = name
        self.age   = age
        self.email = email

    def introduce(self):
        print(f"Hi! I'm {self.name}, {self.age} years old.")

    def get_info(self):
        return f"{self.name} | {self.email}"

# ── CHILD class: inherits from Person ────────────────────────────
class Student(Person):
    """Student inherits from Person."""

    def __init__(self, name, age, email, student_id, marks):
        super().__init__(name, age, email)  # call parent __init__!
        self.student_id = student_id        # student-specific
        self.marks      = marks

    def get_percentage(self):
        return (sum(self.marks) / (len(self.marks) * 100)) * 100

    # Override parent method → customize for Student
    def introduce(self):
        super().introduce()     # call parent version first
        print(f"   I'm a student. ID: {self.student_id}")

class Teacher(Person):
    """Teacher also inherits from Person."""

    def __init__(self, name, age, email, subject, salary):
        super().__init__(name, age, email)
        self.subject = subject
        self.salary  = salary

    def teach(self):
        print(f"👨‍🏫 {self.name} is teaching {self.subject}.")

    def introduce(self):
        super().introduce()
        print(f"   I teach {self.subject}.")

# ── Using inheritance ─────────────────────────────────────────────
student = Student("Ali Hassan", 22,
                  "ali@fast.edu", "STU001",
                  [88, 76, 92, 65, 95])

teacher = Teacher("Dr. Ahmed", 45,
                  "ahmed@fast.edu",
                  "Data Science", 150000)

student.introduce()     # uses Student's version
teacher.introduce()     # uses Teacher's version

# Student has ALL Person methods + its own
print(student.get_info())       # from Person ✅
print(student.get_percentage()) # from Student ✅

teacher.teach()                 # from Teacher ✅
print(teacher.get_info())       # from Person ✅
