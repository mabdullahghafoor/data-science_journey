# In this we will se how to use basic lambda with map function

# ── map() applies a function to EVERY item in a list ─────────────
# Returns a map object — convert to list to see results

marks = [88, 76, 92, 65, 95, 45, 38]

# ── Convert marks to percentages ─────────────────────────────────
percentages = list(map(lambda m: (m / 100) * 100, marks))
print(percentages)      # [88.0, 76.0, 92.0, 65.0, 95.0, 45.0, 38.0]

# ── Add 5 bonus marks to everyone ────────────────────────────────
bonus_marks = list(map(lambda m: min(m + 5, 100), marks))
print(bonus_marks)      # [93, 81, 97, 70, 100, 50, 43]
#                          ↑ min() ensures no one exceeds 100

# ── Convert all names to uppercase ───────────────────────────────
names = ["ali hassan", "sara ahmed", "fatima khan"]
upper = list(map(lambda n: n.title(), names))
print(upper)   

# ── Normal function vs map+lambda ────────────────────────────────
# Without map (loop)
result = []
for m in marks:
    result.append(m * 2)

# With map + lambda (one line!) ✅
result = list(map(lambda m: m * 2, marks))

