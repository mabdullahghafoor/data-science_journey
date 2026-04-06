#In this program we will see some operations regarding sets

# ── Setup: two groups of students ───────────────────────────────
python_students = {"Ali", "Sara", "Fatima", "Omar", "Zara"}
sql_students    = {"Sara", "Omar", "Bilal", "Hina", "Fatima"}


# ── UNION ( | ) → ALL students from BOTH groups ─────────────────
all_students = python_students | sql_students
print(f"All students      : {all_students}")
# {'Ali','Sara','Fatima','Omar','Zara','Bilal','Hina'}


