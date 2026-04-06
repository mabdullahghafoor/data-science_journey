#In this program we will see how to add and remove items in sets

# ── Sets are mutable — you CAN add/remove ───────────────────────
skills = {"Python", "SQL", "Excel"}

# ── Adding ──────────────────────────────────────────────────────
skills.add("PowerBI")           # adds ONE item
print(skills)                   # {'Python', 'SQL', 'Excel', 'PowerBI'}

skills.add("Python")            # duplicate → silently ignored!
print(len(skills))              # still 4

skills.update(["ML", "Tableau"])  # adds MULTIPLE items at once
print(skills)


# ── Removing ────────────────────────────────────────────────────
skills.remove("Excel")          # ❌ raises KeyError if not found!
skills.discard("Excel")         # ✅ safe — no error if not found

popped = skills.pop()           # removes & returns a RANDOM item
print(f"Removed: {popped}")     # you don't know which one!

skills.clear()                  # removes everything
print(skills)                   # set()
