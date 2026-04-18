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