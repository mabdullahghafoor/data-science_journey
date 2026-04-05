# In this we will se a real word examplehow can we use tuple in data science

# ── Tuples as fixed database records ────────────────────────────
# In real databases, each row is a fixed record — perfect for tuple

students_db = [
    ("STU001", "Ali Hassan",  22, 3.87),
    ("STU002", "Sara Ahmed",  21, 3.52),
    ("STU003", "Fatima Khan", 23, 3.95),
    ("STU004", "Omar Farooq", 22, 2.89),
]

# Each record is a tuple — data is safe, cannot be accidentally changed

print("╔══════════════════════════════════════════╗")
print("         🎓 STUDENT DATABASE                ")
print("╠══════════════════════════════════════════╣")

for record in students_db:
    roll, name, age, cgpa = record      # tuple unpacking!
    status = "⭐ Dean's List" if cgpa >= 3.7 else "Regular"
    print(f"  [{roll}] {name:<15} | CGPA: {cgpa} | {status}")

print("╚══════════════════════════════════════════╝")