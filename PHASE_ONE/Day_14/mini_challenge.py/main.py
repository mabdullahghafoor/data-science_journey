from student import Student
from classroom import Classroom


c1 = Classroom("BS Software Engineering")


s1 = Student(1, "Ali")
s1.add_marks("Math", 90)
s1.add_marks("Python", 85)
s1.add_marks("OOP", 80)

s2 = Student(2, "Sara")
s2.add_marks("Math", 95)
s2.add_marks("Python", 92)
s2.add_marks("OOP", 89)

s3 = Student(3, "Ahmed")
s3.add_marks("Math", 40)
s3.add_marks("Python", 45)
s3.add_marks("OOP", 35)


c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)

c1.generate_report()

print("\nTopper:")
print(c1.get_topper())

print("\nFailures:")
for student in c1.get_failures():
    print(student)
