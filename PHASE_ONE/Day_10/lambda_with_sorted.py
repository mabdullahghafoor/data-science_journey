# In this we will se how to use basic lambda with sorted

# ── This is the #1 real-world use of lambda ───────────────────────
# sorted() has a 'key' parameter — you tell it HOW to sort

students = [
    {"name": "Ali",    "cgpa": 3.87, "age": 22},
    {"name": "Sara",   "cgpa": 3.52, "age": 21},
    {"name": "Fatima", "cgpa": 3.95, "age": 23},
    {"name": "Omar",   "cgpa": 2.89, "age": 22},
    {"name": "Zara",   "cgpa": 3.71, "age": 20},
]


# ── Sort by CGPA (highest first) ─────────────────────────────────
by_cgpa = sorted(students,
                 key=lambda s: s["cgpa"],
                 reverse=True)

print("📊 Sorted by CGPA:")
for s in by_cgpa:
    print(f"  {s['name']:<10}: {s['cgpa']}")

# ── Sort by NAME alphabetically ───────────────────────────────────
by_name = sorted(students, key=lambda s: s["name"])
print("\n📊 Sorted by Name:")
for s in by_name:
    print(f"  {s['name']}")

# ── Sort by AGE then CGPA (multiple keys!) ────────────────────────
by_age_cgpa = sorted(students,
                     key=lambda s: (s["age"], s["cgpa"]))
print("\n📊 Sorted by Age then CGPA:")
for s in by_age_cgpa:
    print(f"  {s['name']:<10}: Age={s['age']} CGPA={s['cgpa']}")