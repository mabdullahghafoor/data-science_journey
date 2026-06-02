# ── Package structure ────────────────────────────────────────────
#
# student_system/          ← PACKAGE (folder)
# │
# ├── __init__.py          ← marks this as a package (can be empty)
# ├── utils.py             ← utility functions
# ├── grades.py            ← grading functions
# ├── reports.py           ← report generation
# └── main.py              ← main program
#

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
            return grade
    return "F"
