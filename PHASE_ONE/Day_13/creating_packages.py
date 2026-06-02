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

# FILE: reports.py
from datetime import datetime

def generate_report_header(title):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'═'*45}")
    print(f"  {title}")
    print(f"  Generated: {timestamp}")
    print(f"{'═'*45}")

# FILE: main.py — using the package
from student_system import utils
from student_system.grades import assign_grade
from student_system.reports import generate_report_header

