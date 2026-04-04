# In this program we will see some practice examples using enumerate and zip


# ── enumerate: gives index AND value together ───────────────────

subjects = ["Math", "English", "Science", "Urdu", "CS"]
marks    = [88, 76, 92, 65, 95]

# Beginner way

for i in range(len(subjects)):
    print(f"{i+1}. {subjects[i]} : {marks[i]}")

# Python way with enumerate

for index,subject in enumerate(subjects,start = 1):
    print(f"{index}. {subject}")


# ── zip: loops through TWO lists at same time ───────────────────
# ✅ Even better — combine both lists

for subject,mark in zip(subjects,marks):
    status = "Pass" if mark >= 40 else "Fail"
    print(f"{subject: <15} : {mark: >3}/100 {status}")