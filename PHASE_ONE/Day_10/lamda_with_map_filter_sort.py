# In this we will se how to use basic lambda with map plus filter plus sort function together

# ── Real Data Science pipeline in 3 lines ────────────────────────
# This is EXACTLY how you process data in pandas/python

raw_marks = [88, 45, 92, 32, 78, 65, 55, 90, 28, 73, 38, 82]

# Step 1: Add 5 bonus marks (map)
with_bonus = list(map(lambda m: min(m + 5, 100), raw_marks))

# Step 2: Keep only passing marks (filter)
passing = list(filter(lambda m: m >= 50, with_bonus))

# Step 3: Sort highest to lowest (sorted)
final = sorted(passing, key=lambda m: m, reverse=True)

print(f"Original : {raw_marks}")
print(f"Bonus    : {with_bonus}")
