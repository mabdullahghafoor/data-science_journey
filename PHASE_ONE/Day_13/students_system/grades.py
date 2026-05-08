# In this we will see how to create our own package

# FILE: grades.py
def assign_grade(percentage):
    grades = {
        range(90, 101): "A+",
        range(80, 90) : "A",
        range(70, 80) : "B",
        range(60, 70) : "C",
        range(50, 60) : "D",
    }
    for mark_range, grade in grades.items():
        if int(percentage) in mark_range:
