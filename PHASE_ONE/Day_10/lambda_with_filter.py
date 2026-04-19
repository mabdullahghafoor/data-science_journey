# In this we will se how to use basic lambda with filter function

# ── filter() keeps ONLY items where function returns True ─────────

marks    = [88, 45, 92, 32, 78, 65, 55, 90, 28, 73]
students = ["Ali", "Sara", "Fatima", "Omar", "Zara"]

# ── Keep only passing marks (>= 50) ──────────────────────────────
passed = list(filter(lambda m: m >= 50, marks))
print(f"Passed marks : {passed}")
# [88, 92, 78, 65, 55, 90, 73]