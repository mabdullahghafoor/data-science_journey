# In this we will se how to use basic lambda with filter function

# ── filter() keeps ONLY items where function returns True ─────────

marks    = [88, 45, 92, 32, 78, 65, 55, 90, 28, 73]
students = ["Ali", "Sara", "Fatima", "Omar", "Zara"]

# ── Keep only passing marks (>= 50) ──────────────────────────────
passed = list(filter(lambda m: m >= 50, marks))
print(f"Passed marks : {passed}")
# [88, 92, 78, 65, 55, 90, 73]

# ── Keep only failed marks ────────────────────────────────────────
failed = list(filter(lambda m: m < 50, marks))
print(f"Failed marks : {failed}")
# [45, 32, 28]

# ── Filter names starting with a specific letter ──────────────────
f_names = list(filter(lambda n: n.startswith("F"), students))
print(f"Names with F : {f_names}")
# ['Fatima']

# ── Filter marks above class average ─────────────────────────────
average      = sum(marks) / len(marks)
above_avg    = list(filter(lambda m: m > average, marks))
print(f"Average      : {average:.1f}")
print(f"Above average: {above_avg}")