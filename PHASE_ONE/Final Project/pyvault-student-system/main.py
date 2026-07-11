# ═══════════════════════════════════════════════════
# FILE    : main.py
# PROJECT : PyVault — Student Management System
# AUTHOR  : Your Name
# PHASE   : 1 — Python Foundation (Final Project)
# USES    : ALL 15 TOPICS
# ═══════════════════════════════════════════════════

import os
from datetime import datetime
from models.students    import Student
from models.classroom  import Classroom
from utils.validators  import (get_input, get_int,
                                validate_email,
                                validate_student_id)
from utils.analytics   import (get_top_n_stack,
                                announcement_queue,
                                grade_frequency_hashmap)

# ── Initialize classroom ──────────────────────────────────────────
classroom = Classroom()


# ── Logging ───────────────────────────────────────────────────────
def log_activity(action):
    """Log every action to file — File Handling."""
    os.makedirs("data/logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data/logs/activity.log", "a",
              encoding="utf-8") as f:
        f.write(f"[{timestamp}] {action}\n")


# ── Display Helpers ───────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_header(title):
    print(f"\n  {'═'*46}")
    print(f"      {title}")
    print(f"  {'═'*46}")

def print_line():
    print(f"  {'─'*46}")


# ════════════════════════════════════════════
#   FEATURE 1 — Add Student
# ════════════════════════════════════════════
def add_student():
    print_header("➕ ADD NEW STUDENT")
    try:
        sid   = validate_student_id(
                    get_input("  Student ID (e.g. STU001): "))
        name  = get_input("  Full Name  : ")
        age   = get_int("  Age        : ", 15, 80)
        city  = get_input("  City       : ")
        email = validate_email(
                    get_input("  Email      : "))

        student = Student(sid, name, age, city, email)
        classroom.add_student(student)
        log_activity(f"Added student: {name} [{sid}]")

    except (ValueError, KeyError) as e:
        print(f"\n  ❌ Error: {e}")


# ════════════════════════════════════════════
#   FEATURE 2 — Enter Marks
# ════════════════════════════════════════════
def enter_marks():
    print_header("📝 ENTER MARKS")
    try:
        sid     = get_input("  Enter Student ID: ").upper()
        student = classroom.get_student(sid)
        print(f"\n  Entering marks for: {student.name}")
        print_line()

        for subject in Student.SUBJECTS:
            marks = get_int(
                f"  {subject:<15}: ", 0, 100
            )
            classroom.add_marks(sid, subject, marks)

        log_activity(f"Marks entered for: {student.name}")
        print(f"\n  ✅ All marks saved!")
        student.print_card()

    except (KeyError, ValueError) as e:
        print(f"\n  ❌ Error: {e}")


# ════════════════════════════════════════════
#   FEATURE 3 — View Student
# ════════════════════════════════════════════
def view_student():
    print_header("🔍 VIEW STUDENT")
    try:
        sid     = get_input("  Enter Student ID: ").upper()
        student = classroom.get_student(sid)
        student.print_card()
        log_activity(f"Viewed: {student.name}")
    except KeyError as e:
        print(f"\n  ❌ {e}")


# ════════════════════════════════════════════
#   FEATURE 4 — View All Students
# ════════════════════════════════════════════
def view_all():
    print_header("📋 ALL STUDENTS")
    students = classroom.get_all_students()

    if not students:
        print("\n  No students found.")
        return
