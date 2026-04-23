#In this program we will see how to use and access CSV files

# ── CSV = Comma Separated Values ─────────────────────────────────
# The most common data format in Data Science!
# Every spreadsheet, dataset, database export = CSV

import csv

# ── Writing CSV ───────────────────────────────────────────────────
students = [
    ["Name",    "Marks", "Grade", "Status"],    # header row
    ["Ali",     88,      "A",     "Pass"],
    ["Sara",    45,      "F",     "Fail"],
    ["Fatima",  97,      "A+",    "Pass"],
    ["Omar",    32,      "F",     "Fail"],
    ["Zara",    78,      "B",     "Pass"],
]

with open("Students.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerows(students)

print("CSV File Written Successfully!")