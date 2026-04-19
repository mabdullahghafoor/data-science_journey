# In this we will se how to use basic lambda with map function

# ── map() applies a function to EVERY item in a list ─────────────
# Returns a map object — convert to list to see results

marks = [88, 76, 92, 65, 95, 45, 38]

# ── Convert marks to percentages ─────────────────────────────────
percentages = list(map(lambda m: (m / 100) * 100, marks))
print(percentages)      # [88.0, 76.0, 92.0, 65.0, 95.0, 45.0, 38.0]