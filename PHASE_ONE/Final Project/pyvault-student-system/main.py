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

    print(f"\n  {'ID':<10} {'Name':<20} {'%':>6} "
          f"{'Grade':>6} {'Status'}")
    print_line()

    for s in sorted(students, key=lambda x: x.student_id):
        pct   = f"{s.percentage}%" if s.has_marks() else "N/A"
        grade = s.grade if s.has_marks() else "N/A"
        print(f"  {s.student_id:<10} {s.name:<20} "
              f"{pct:>6} {grade:>6}  {s.status}")

    print_line()
    print(f"  Total: {classroom.total_students()} students")


# ════════════════════════════════════════════
#   FEATURE 5 — Search Students
# ════════════════════════════════════════════
def search_students():
    print_header("🔎 SEARCH STUDENTS")
    query   = get_input("  Enter name to search: ")
    results = classroom.search_by_name(query)

    if not results:
        print(f"\n  ❌ No students found for '{query}'")
        return

    print(f"\n  Found {len(results)} result(s):\n")
    for s in results:
        print(f"  → {s}")


# ════════════════════════════════════════════
#   FEATURE 6 — Delete Student
# ════════════════════════════════════════════
def delete_student():
    print_header("🗑️  DELETE STUDENT")
    try:
        sid     = get_input("  Enter Student ID: ").upper()
        student = classroom.get_student(sid)
        confirm = get_input(
            f"\n  Delete '{student.name}'? (yes/no): "
        ).lower()

        if confirm == "yes":
            classroom.delete_student(sid)
            log_activity(f"Deleted: {student.name} [{sid}]")
        else:
            print("\n  ❌ Deletion cancelled.")

    except KeyError as e:
        print(f"\n  ❌ {e}")


# ════════════════════════════════════════════
#   FEATURE 7 — Class Analytics
# ════════════════════════════════════════════
def class_analytics():
    print_header("📊 CLASS ANALYTICS")
    students = classroom.get_all_students()

    if not students:
        print("\n  No students to analyze.")
        return

    ranked   = classroom.get_ranked()
    topper   = classroom.get_topper()
    failures = classroom.get_failures()
    avg      = classroom.class_average()
    dist     = classroom.grade_distribution()
    subj_avg = classroom.subject_averages()

    print(f"\n  Total Students : {classroom.total_students()}")
    print(f"  Class Average  : {avg}%")

    if topper:
        print(f"  🏆 Topper      : {topper.name} "
              f"({topper.percentage}%)")
    print(f"  ❌ Failures    : {len(failures)}")

    # Grade distribution with bar chart
    print(f"\n  GRADE DISTRIBUTION:")
    print_line()
    grade_order = ["A+","A","B","C","D","F"]
    for grade in grade_order:
        count = dist.get(grade, 0)
        bar   = "█" * count
        print(f"  {grade:<4}: {bar:<20} ({count})")

    # Subject averages
    if subj_avg:
        print(f"\n  SUBJECT AVERAGES:")
        print_line()
        for subject, avg_mark in subj_avg.items():
            bar = "█" * int(avg_mark // 10)
            print(f"  {subject:<12}: {bar:<10} {avg_mark}%")

    log_activity("Viewed class analytics")


# ════════════════════════════════════════════
#   FEATURE 8 — Rankings
# ════════════════════════════════════════════
def show_rankings():
    print_header("🏆 STUDENT RANKINGS")
    students = [s for s in classroom.get_all_students()
                if s.has_marks()]

    if not students:
        print("\n  No marks entered yet.")
        return

    # Use STACK to get top 5
    top5 = get_top_n_stack(students, 5)

    print("\n  🥇 TOP 5 STUDENTS (via Stack DSA):\n")
    medals = ["🥇","🥈","🥉","4️⃣ ","5️⃣ "]
    for i, student in enumerate(top5):
        print(f"  {medals[i]} {student.name:<18} "
              f": {student.percentage}%  {student.grade}")

    # Full ranking
    print(f"\n  📋 FULL CLASS RANKING:\n")
    ranked = classroom.get_ranked()
    for i, student in enumerate(ranked, 1):
        print(f"  {i:>3}. {student.name:<18} "
              f": {student.percentage}%  {student.grade}")

    log_activity("Viewed rankings")


# ════════════════════════════════════════════
#   FEATURE 9 — Export Report
# ════════════════════════════════════════════
