# In this program we will see some examples regarding dictionary comprehension

# ── Regular way to build a dictionary ────────────────────────────
students = ["Ali", "Sara", "Fatima", "Omar"]
marks    = [88, 65, 97, 45]

gradebook = {}
for student, mark in zip(students, marks):
    gradebook[student] = mark
print(gradebook)    # {'Ali':88, 'Sara':65, 'Fatima':97, 'Omar':45} 