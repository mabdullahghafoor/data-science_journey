# In this we will se how to use lambda functio in Real World Basic things

# ── Use Case 1: Sort products by price ───────────────────────────
products = [
    ("Laptop",  85000),
    ("Mouse",    1500),
    ("Keyboard", 3500),
    ("Monitor", 45000),
    ("Webcam",   8000),
]

cheapest   = sorted(products, key=lambda p: p[1])
expensive  = sorted(products, key=lambda p: p[1], reverse=True)

print("💸 Cheapest first:")
for name, price in cheapest:
    print(f"  {name:<12}: PKR {price:,}")

# ── Use Case 2: Grade all students in one line ────────────────────
percentages = [88.5, 45.2, 92.1, 32.8, 78.0]

grades = list(map(
    lambda p: "A+" if p >= 90 else
              "A"  if p >= 80 else
              "B"  if p >= 70 else
              "C"  if p >= 60 else
              "D"  if p >= 50 else "F",
    percentages
))
print(grades)   # ['A', 'F', 'A+', 'F', 'B']

# ── Use Case 3: Filter valid emails ──────────────────────────────
emails = ["ali@gmail.com", "invalid-email",
          "sara@yahoo.com", "notanemail", "omar@fast.edu"]