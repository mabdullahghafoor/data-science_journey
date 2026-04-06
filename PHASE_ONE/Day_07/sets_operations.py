#In this program we will see some operations regarding sets

# ── Setup: two groups of students ───────────────────────────────
python_students = {"Ali", "Sara", "Fatima", "Omar", "Zara"}
sql_students    = {"Sara", "Omar", "Bilal", "Hina", "Fatima"}


# ── UNION ( | ) → ALL students from BOTH groups ─────────────────
all_students = python_students | sql_students
print(f"All students      : {all_students}")
# {'Ali','Sara','Fatima','Omar','Zara','Bilal','Hina'}


# ── INTERSECTION ( & ) → students in BOTH courses ───────────────
both = python_students & sql_students
print(f"Enrolled in both  : {both}")
# {'Sara', 'Omar', 'Fatima'}


# ── DIFFERENCE ( - ) → ONLY in Python, NOT in SQL ───────────────
only_python = python_students - sql_students
print(f"Only Python       : {only_python}")
# {'Ali', 'Zara'}

only_sql = sql_students - python_students
print(f"Only SQL          : {only_sql}")
# {'Bilal', 'Hina'}


# ── SYMMETRIC DIFFERENCE ( ^ ) → in ONE but NOT BOTH ────────────
exclusive = python_students ^ sql_students
print(f"In one only       : {exclusive}")
# {'Ali', 'Zara', 'Bilal', 'Hina'}


