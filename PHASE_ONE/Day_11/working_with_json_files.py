#In this program we will see how to use and access JSON files

# ── JSON = JavaScript Object Notation ────────────────────────────
# How APIs send data, how configs are stored
# Python dict ↔ JSON are almost identical!

import json

# ── Writing JSON ──────────────────────────────────────────────────

student_data = {
    "students": [
        {"id": "STU001", "name": "Ali Hassan",
         "marks": [88, 76, 92], "cgpa": 3.87},
        {"id": "STU002", "name": "Sara Ahmed",
         "marks": [65, 82, 71], "cgpa": 3.52},
        {"id": "STU003", "name": "Fatima Khan",
         "marks": [95, 98, 100], "cgpa": 3.95},
    ],
    "total_students": 3,
    "institution": "FAST-NUCES"
}

with open("Students.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("JSON File written Successfully!")